import os
import sys
import cv2
from app import faceswap

def read_image_files(file_face, file_body):
    img_face = cv2.imread(file_face)
    img_body = cv2.imread(file_body)

    return img_face, img_body

if len(sys.argv) != 3:
    print('Requires a \'face\' and a \'body\' image.')
    sys.exit()

file_face = sys.argv[1]
file_body = sys.argv[2]

img_face, img_body = read_image_files(file_face, file_body)
result = faceswap(img_face, img_body)

cv2.imwrite("/data/result.png", result)
