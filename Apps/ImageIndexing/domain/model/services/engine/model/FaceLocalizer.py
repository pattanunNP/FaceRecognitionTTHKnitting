from cv2 import log
from facenet_pytorch import MTCNN
from engine.utils.log import Logger


class FaceLocalizer:
    """
    Face Localizer
    --------------

    Params
    ------

    - margin : [int] default =  5
    - min_face_size : [int] default =  40


    """

    def __init__(
        self,
                 margin=5,
                 log_file="../run.log",
                 Logger=Logger):

        self.Logger = Logger(name="FaceLocalizer", level="info",
                             log_file=log_file, save_to_file="True")

        self.facenet = MTCNN(margin=margin)
        self.Logger.info(f"Face Localizier Initialized")

    def detect_faces(self, img) -> dict:
        """
        Methods :
        -------

        - detect_faces

        Args :
        ----
            - img : [np.array]

        Return :
        ------
            - dict of face and attibute

        """
        faces = {}
        i = 0

        self.Logger.debug(f"{img}")
        detected_faces = self.facenet.detect(img, landmarks=True)
        self.Logger.debug(f"{detected_faces}")

        if any(map(lambda x: x is None, faces)) == False:

            faces_box = detected_faces[0]
            faces_conf = detected_faces[1]
            landmarks = detected_faces[2]

            try:

                for face_box, face_conf, landmark in zip(faces_box, faces_conf, landmarks):
                    #     print(i,face_box,face_conf,landmark )

                    right_eye = (round(landmark[0][0]), round(landmark[0][1]))
                    left_eye = (round(landmark[1][0]), round(landmark[1][1]))

                    x, y, w, h = round(face_box[0]), round(
                        face_box[1]), round(face_box[2]), round(face_box[3])

                    bbox = {
                        "x": x, "y": y, "w": w-x, "h": h-y,
                    }
                    face_attibute = {
                        "face_box": bbox, "confident": float(face_conf), "right_eye": right_eye, "left_eye": left_eye
                    }
                    faces[i] = face_attibute

                    i += 1
                # print(faces)
            except Exception as err:
                self.Logger.warn(f"[Not Detect Face]: {err}")

        return faces
