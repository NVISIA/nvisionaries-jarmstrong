from flask import Flask, request, jsonify
from io import BytesIO
import numpy as np
import copy
import cv2
import base64
import requests
import json
import tensorflow as tf
from app import faceswap

f_app = Flask(__name__)
f_app.secret_key = "nvisia"

jedi_sith_url = "http://jedi_sith:8501/v1/models/jedi_sith"
rembg_url = "http://rembg:5000"
eventsink_url = "https://edsf.itwasaday.net/api/boothEvents"
eventsink_auth_key = "3a1d287e-7e57-464c-b0b5-e6595ece0b6b"

EVENTSINK_HEADER_NAME = "Authorization"
TF_INPUT_SHAPE = [200, 200] #1D tensor
TF_INPUT_DTYPE = tf.float32

def keras_img_to_array(img, data_format=None, dtype=None):
    # Copied from Keras 2.11.0
    if data_format is None:
        data_format = 'channels_last'
    if dtype is None:
        dtype = "float32"
    if data_format not in {"channels_first", "channels_last"}:
        raise ValueError(f"Unknown data_format: {data_format}")
    # Numpy array x has format (height, width, channel)
    # or (channel, height, width)
    # but original PIL image has format (width, height, channel)
    x = np.asarray(img, dtype=dtype)
    if len(x.shape) == 3:
        if data_format == "channels_first":
            x = x.transpose(2, 0, 1)
    elif len(x.shape) == 2:
        if data_format == "channels_first":
            x = x.reshape((1, x.shape[0], x.shape[1]))
        else:
            x = x.reshape((x.shape[0], x.shape[1], 1))
    else:
        raise ValueError(f"Unsupported image shape: {x.shape}")
    return x

def dispatch_to_jedi_sith(img):
    # convert color order because OpenCV uses BGR for some reason
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # resize
    img_array = keras_img_to_array(img)
    img_array = img_array[:,:,:3]
    img_array = tf.image.resize(img_array, TF_INPUT_SHAPE)
    img_array = tf.image.convert_image_dtype(img_array, tf.float32)
    img_np = img_array.numpy().tolist()

    # dispatch to jedi_sith
    headers = {"content-type": "application/json"}
    data = json.dumps({"signature_name": "serving_default", "instances": [img_np]})
    json_response = requests.post(jedi_sith_url + ":predict", data=data, headers=headers)
    predictions = json.loads(json_response.text)['predictions']
    prediction = predictions[0]
    score = prediction[0]

    return score

def remove_background(image):
    files = {'file': image}
    headers = {'User-Agent': 'faceswap-api'}
    r = requests.post(rembg_url, files=files, headers=headers)
    buffer = BytesIO(r.content)
    image_str = buffer.getvalue()

    return image_str

def process_file(file):
    img_string = file
    img_string = base64.b64decode(img_string)
    img_string = remove_background(img_string)
    img_array = np.fromstring(img_string, np.uint8)
    img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)

    return img

def get_body_image(score):
    filename = f'/data/{score}.png'
    img = cv2.imread(filename, cv2.IMREAD_COLOR)

    return img

def sink_event(json_data):
    headers = {EVENTSINK_HEADER_NAME: eventsink_auth_key, "content-type": "application/json"}
    data = json.dumps({"messageType": "sithjedi", "message": "photo", "json": json.dumps(json_data)})
    requests.post(eventsink_url, data=data, headers=headers)

def resize_image(image, new_width=1080):
    orig_height, orig_width, _ = image.shape
    scale_factor = new_width / orig_width
    new_height = int(orig_height * scale_factor)
    new_dim = (new_width, new_height)

    return cv2.resize(image, new_dim, interpolation=cv2.INTER_AREA)

@f_app.route("/", methods=["POST"])
def post():
    # decode file and get score
    file = request.form.get('file')
    face_img = process_file(file)
    score = dispatch_to_jedi_sith(face_img)

    # select body_img using score as an index
    score_offset = score * 10
    score_idx = round(score_offset)
    body_img = get_body_image(score_idx)
    
    # faceswap!
    result = faceswap(face_img, body_img)

    # resize to uniform size
    result = resize_image(result, 576)

    # base64 encode result
    _, image_buffer = cv2.imencode(".png", result)
    b64_result = base64.b64encode(image_buffer)
    result_string = b64_result.decode('utf-8')
    json_response = {"score": score, "image": result_string}

    # sink event to George
    sink_event(json_response)

    return jsonify(json_response)

if __name__ == "__main__":
    f_app.run(host='0.0.0.0', port=5000)
