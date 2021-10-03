import cv2
import numpy as np


class FaceImagePreprocessing:
    """
    FaceImagePreprocessing
    ----------------------


    """

    @staticmethod
    def cropface(image, facelocation):
        """
        Method
        ------
        Crop face from image

        Args:
        -----

        - image : [np.array]
        - faceloaction : [dict]

        Return:
        ------

        - Cropped Face : [np.array]

        """
        bbox = facelocation['face_box']
        x = bbox['x']
        y = bbox['y']
        w = bbox['w']
        h = bbox['h']

        return image[y:y+h, x:x+w]

    @staticmethod
    def alignface(cropped_face, facelocation):
        """
        Method
        ------
        For rotate and align face 

        Args:
        -----

        - croppedface : [np.array]
        - faceloaction : [dict]

        Return:
        ------

        - Aligned Face : [np.array]

        """

        f_h = cropped_face.shape[0]
        f_w = cropped_face.shape[1]

        left_eye, right_eye = facelocation['left_eye'], facelocation['right_eye']

        left_eye_x, left_eye_y = left_eye
        right_eye_x, right_eye_y = right_eye

        delta_x = right_eye_x - left_eye_x

        delta_y = right_eye_y - left_eye_y

        angle = np.arctan(delta_y/delta_x)
        angle = (angle * 180) / np.pi

        center_img = (f_w // 2, f_h // 2)

        M = cv2.getRotationMatrix2D(center_img, (angle), 1.0)

        aligned = cv2.warpAffine(cropped_face, M, (f_w, f_h))

        return aligned
