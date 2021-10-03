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

    def __init__(self,
                 margin=5,
                 min_face_size=40,
                 log_file="run.log",
                 Logger=Logger):

        Logger = Logger(name="FaceLocalizer", level="info",
                        log_file=log_file, save_to_file="True")
        try:
            # Try to initialize MTCNN
            self.mtcnn = MTCNN(
                margin=margin,
                min_face_size=min_face_size,
                post_process=True)

        except Exception as err:
            print(err)

    def detect_faces(self, img) -> dict:
        """
        Methods :
        -------

        Args :
        ----
            - img : [np.array]

        Return :
        ------
            - dict of face and attibute

        """

        faces = self.facenet.detect(img, landmarks=True)
    #     print(faces)

        faces_box = faces[0]
        faces_conf = faces[1]
        landmarks = faces[2]
        face = {}

        for i, (face_box, face_conf, landmark) in enumerate(zip(faces_box, faces_conf, landmarks)):
            #     print(i,face_box,face_conf,landmark )

            right_eye = (round(landmark[0][0]), round(landmark[0][1]))
            left_eye = (round(landmark[1][0]), round(landmark[1][1]))

            x, y, w, h = round(face_box[0]), round(
                face_box[1]), round(face_box[2]), round(face_box[3])

            bbox = {

                "x": x,
                "y": y,
                "w": w,
                "h": h,

            }
            face_attibute = {
                "face_box": bbox,
                "confident": face_conf,
                "right_eye": right_eye,
                "left_eye": left_eye

            }
            face[i] = face_attibute

        return face
