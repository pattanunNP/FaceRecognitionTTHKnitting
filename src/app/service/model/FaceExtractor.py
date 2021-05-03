
from facenet_pytorch import InceptionResnetV1,MTCNN
from app.utils.message import message

class FaceExtractor:


    def __init__(self, model='vggface2',margin=5):
        
        try:
            message.WarnPrint("\nFaceExtractor: Loading Model",end="\r")
            self.mtcnn = MTCNN(image_size=160, margin=margin)
            self.resnet = InceptionResnetV1(pretrained='vggface2').eval()
            message.SuccessPrint("FaceExtractor: Loaded Success", end="\r")
        except Exception as err:
            print(err)

    def extractFeature(self, x):
        try:
            img_cropped = self.mtcnn(x)
            return self.resnet(img_cropped.unsqueeze(0)).cpu().detach().numpy()
        except:
            pass
