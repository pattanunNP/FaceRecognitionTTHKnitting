
from facenet_pytorch import MTCNN
from app.utils.message import message
from area import area

class FaceLocalizer:


    def __init__(self,
                 margin=5,
                 save_path=None):
        try:
            message.WarnPrint("\nFaceLocalizer: Loading Model",end="\r")
            self.mtcnn = MTCNN(image_size=160, margin=margin)
            message.SuccessPrint("FaceLocalizer: Loaded Success", end="\r")
        except Exception as err:
            print(err)
                 

    def Localize(self, x, return_faceCropped=True):

        boxes={}
        face = {}
        try:
            facelocalations,_ = self.mtcnn.detect(x)
            id = 0
            for face_id in facelocalations:
                bbox={

                    "x":face_id[0],
                    "y":face_id[1],
                    "w":face_id[2]-face_id[0],
                    "h":face_id[3]-face_id[1],
                
                }
                face[id] = bbox
                id+=1
        except:
            pass
        return  face
