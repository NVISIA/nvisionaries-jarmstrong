import cv2
import dlib
import numpy as np

def get_landmarks(landmarks, landmarks_points):
    for point_index in range(68):
        x = landmarks.part(point_index).x
        y = landmarks.part(point_index).y
        landmarks_points.append((x, y))

def get_index(arr):
    index = 0

    if arr[0].any():
        index = arr[0][0]

    return index

def to_gray(img_face, img_body):
    img_face_gray = cv2.cvtColor(img_face, cv2.COLOR_BGR2GRAY)
    img_body_gray = cv2.cvtColor(img_body, cv2.COLOR_BGR2GRAY)

    return img_face_gray, img_body_gray

def load_dlib():
    landmarks_data_file = "/data/shape_predictor_68_face_landmarks.dat"
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(landmarks_data_file)

    return detector, predictor

def detect_face(img_gray, detector, predictor, landmarks_points):
    faces = detector(img_gray)

    if len(faces) < 1:
        print("No faces detected")
        return None

    face_rect = faces[0]
    landmarks = predictor(img_gray, face_rect)

    get_landmarks(landmarks, landmarks_points)
    points = np.array(landmarks_points, np.int32)

    return points

def point_to_index(point, points):
    index_point = np.where((points == point).all(axis=1))

    return get_index(index_point)

def delaunay(convexhull, landmarks_points, points):
    convexhull_rect = cv2.boundingRect(convexhull)
    subdivisions = cv2.Subdiv2D(convexhull_rect)
    subdivisions.insert(landmarks_points)
    triangles = subdivisions.getTriangleList()

    triangle_indices = []

    for triangle in triangles:
        point_1 = (triangle[0], triangle[1])
        point_2 = (triangle[2], triangle[3])
        point_3 = (triangle[4], triangle[5])

        index_point_1 = point_to_index(point_1, points)
        index_point_2 = point_to_index(point_2, points)
        index_point_3 = point_to_index(point_3, points)

        if index_point_1 is not None and index_point_2 is not None and index_point_3 is not None:
            vertices = [index_point_1, index_point_2, index_point_3]
            triangle_indices.append(vertices)

    return triangle_indices

def affine_warp(points_1, points_2, cropped_triangle, width, height, cropped_mask, body_new_face, x, y):
    points_1 = np.float32(points_1)
    points_2 = np.float32(points_2)

    # M is a matrix
    M = cv2.getAffineTransform(points_1, points_2)

    dist_triangle = cv2.warpAffine(cropped_triangle, M, (width, height))
    dist_triangle = cv2.bitwise_and(dist_triangle, dist_triangle, mask=cropped_mask)

    body_new_face_rect_area = body_new_face[y: y+height, x: x+width]
    body_new_face_rect_area_gray = cv2.cvtColor(body_new_face_rect_area, cv2.COLOR_BGR2GRAY)

    masked_triangle = cv2.threshold(body_new_face_rect_area_gray, 1, 255, cv2.THRESH_BINARY_INV)
    dist_triangle = cv2.bitwise_and(dist_triangle, dist_triangle, mask=masked_triangle[1])

    body_new_face_rect_area = cv2.add(body_new_face_rect_area, dist_triangle)
    body_new_face[y: y+height, x: x+width] = body_new_face_rect_area

    return body_new_face

def do_masking(img_gray, convexhull, img, body_new_face):
    body_face_mask = np.zeros_like(img_gray)
    body_head_mask = cv2.fillConvexPoly(body_face_mask, convexhull, 255)
    body_face_mask = cv2.bitwise_not(body_head_mask)

    body_maskless = cv2.bitwise_and(img, img, mask=body_face_mask)
    result = cv2.add(body_maskless, body_new_face)

    return result, body_head_mask

def seamless_clone(convexhull, img_composite, img_body, body_head_mask):
    (x, y, width, height) = cv2.boundingRect(convexhull)
    center_point = (int((x+x+width)/2), int((y+y+height)/2))
    clone = cv2.seamlessClone(img_composite, img_body, body_head_mask, center_point, cv2.NORMAL_CLONE)

    return clone

def add_watermark(image):
    # add alpha channel to image
    image = cv2.cvtColor(image, cv2.COLOR_RGB2RGBA)

    # load logo
    logo_image = cv2.imread('/data/logo.png', cv2.IMREAD_UNCHANGED)
    logo_height, logo_width, _ = logo_image.shape
    logo_dims = (logo_width, logo_height)
    image_height, image_width, _ = image.shape

    # place watermark in lower left corner
    watermark_left_x = image_width - logo_width - 20
    watermark_top_y = image_height - logo_height - 10
    watermark_right_x = image_width - 20
    watermark_bottom_y = image_height - 10

    roi = image[watermark_top_y:watermark_bottom_y, watermark_left_x:watermark_right_x]

    # composite
    composite = cv2.addWeighted(roi, 1, logo_image, 0.1, 0)

    # swap in new roi
    image[watermark_top_y:watermark_bottom_y, watermark_left_x:watermark_right_x] = composite

    return image

def faceswap(img_face, img_body):
    img_face_gray, img_body_gray = to_gray(img_face, img_body)

    detector, predictor = load_dlib()

    face_1_landmarks_points = []
    face_1_points = detect_face(img_face_gray, detector, predictor, face_1_landmarks_points)
    face_1_convexhull = cv2.convexHull(face_1_points)
    face_1_triangle_indices = delaunay(face_1_convexhull, face_1_landmarks_points, face_1_points)

    face_2_landmarks_points = []
    face_2_points = detect_face(img_body_gray, detector, predictor, face_2_landmarks_points)
    face_2_convexhull = cv2.convexHull(face_2_points)

    height, width, channels = img_body.shape
    lines_space_new_face = np.zeros((height, width, channels), np.uint8)
    body_new_face = np.zeros((height, width, channels), np.uint8)

    height, width = img_face_gray.shape
    lines_space_mask = np.zeros((height, width), np.uint8)
    healed_result = None

    for triangle_index in face_1_triangle_indices:
        point_1 = face_1_landmarks_points[triangle_index[0]]
        point_2 = face_1_landmarks_points[triangle_index[1]]
        point_3 = face_1_landmarks_points[triangle_index[2]]

        (x, y, width, height) = cv2.boundingRect(np.array([point_1, point_2, point_3], np.int32))
        cropped_triangle = img_face[y: y+height, x: x+width]
        cropped_mask_1 = np.zeros((height, width), np.uint8)

        points_1 = np.array([[point_1[0]-x, point_1[1]-y], [point_2[0]-x, point_2[1]-y], [point_3[0]-x, point_3[1]-y]], np.int32)
        cv2.fillConvexPoly(cropped_mask_1, face_1_points, 255)

        cv2.line(lines_space_mask, point_1, point_2, 255)
        cv2.line(lines_space_mask, point_2, point_3, 255)
        cv2.line(lines_space_mask, point_1, point_3, 255)

        lines_space = cv2.bitwise_and(img_face, img_face, mask=lines_space_mask)

        point_1 = face_2_landmarks_points[triangle_index[0]]
        point_2 = face_2_landmarks_points[triangle_index[1]]
        point_3 = face_2_landmarks_points[triangle_index[2]]

        (x, y, width, height) = cv2.boundingRect(np.array([point_1, point_2, point_3], np.int32))
        cropped_mask_2 = np.zeros((height, width), np.uint8)

        points_2 = np.array([[point_1[0]-x, point_1[1]-y], [point_2[0]-x, point_2[1]-y], [point_3[0]-x, point_3[1]-y]], np.int32)
        cv2.fillConvexPoly(cropped_mask_2, points_2, 255)

        body_new_face = affine_warp(points_1, points_2, cropped_triangle, width, height, cropped_mask_2, body_new_face, x, y)
        result, body_head_mask = do_masking(img_body_gray, face_2_convexhull, img_body, body_new_face)
        healed_result = seamless_clone(face_2_convexhull, result, img_body, body_head_mask)
        with_added_watermark = add_watermark(healed_result)

    return with_added_watermark
