from pathlib import Path
from libs import KafkaProducer
from PIL import Image
from base64 import b64encode

class RequestProducer:
    def __init__(self):
        self.messageQueue =  KafkaProducer(topic_name="face-recognition")
    
                                                
    def run(self, path:str):
        print("running")
        path = Path(path).absolute()

        for image_path in path.glob('**/*.jpg'):      
            print("Sending image: ", image_path)
            with open(image_path, 'rb') as image_file:
                image = image_file.read()
                self.messageQueue.serializeImg(image)
                self.messageQueue.send(image)
           
            


if __name__ == "__main__":
    rp = RequestProducer()
    rp.run("/Users/arm/Code/Projects/Freelance/TTH/FaceRecognitionTTHKnitting/Runner")    
