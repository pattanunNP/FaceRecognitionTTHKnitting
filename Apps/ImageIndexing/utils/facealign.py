import numpy as np
import cv2


class FaceAlign:

    @staticmethod
    def align_face(image_path, face):

        img = cv2.imread(image_path)
        face_pos = face['face_box']

        right_eye_pos = face['right_eye']
        left_eye_pos = face['left_eye']

        x = face_pos['x']
        y = face_pos['y']
        w = face_pos['w']
        h = face_pos['h']

        left_eye_x, left_eye_y = left_eye_pos
        right_eye_x, right_eye_y = right_eye_pos

        if left_eye_y < right_eye_y:
            point_3rd = (right_eye_x, left_eye_y)
            direction = -1
        else:
            point_3rd = (left_eye_x, right_eye_y)
            direction = 1

        delta_x = right_eye_x - left_eye_x
        delta_y = right_eye_y - left_eye_y
        angle = np.arctan(delta_y/delta_x)
        angle = (angle * 180) / np.pi

        img = img[y:y+h, x:x+w]

        f_h = img.shape[0]
        f_w = img.shape[1]

        center_img = (f_w // 2, f_h // 2)

        M = cv2.getRotationMatrix2D(center_img, angle, 1.0)

        rotated = cv2.warpAffine(img, M, (f_w, f_h))

        return rotated
