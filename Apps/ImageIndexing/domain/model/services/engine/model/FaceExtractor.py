
from json import encoder
from typing import Any
from facenet_pytorch import InceptionResnetV1, MTCNN
from engine.utils.facealign import FaceAlign


class FaceExtractor:

    def __init__(self, model='vggface2', margin=5):

        try:
            # message.WarnPrint("\nFaceExtractor: Loading Model",end="\r")
            self.mtcnn = MTCNN(image_size=160, margin=margin)
            self.resnet = InceptionResnetV1(pretrained='vggface2').eval()
            # message.SuccessPrint("FaceExtractor: Loaded Success", end="\r")
        except Exception as err:
            print(err)

    def extractFeature(self, image_path, face_id, face_cord):

        aligned = FaceAlign.align_face(image_path, face_cord)
        face_tensor = self.mtcnn(aligned)
        encoded_face = self.resnet(
            face_tensor.unsqueeze(0)).cpu().detach().numpy()
        print(encoded_face)
