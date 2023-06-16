import time
from base64 import b64encode
from pathlib import Path
import cv2
import numpy as np
from loguru import logger
from infrastructure import KafkaProducer
from utils import compress_img, BuildMessage
from tqdm.auto import tqdm


class Producer:

    def __init__(self):
        self.messageQueue = KafkaProducer(topic_name="face-recognition")

    def run(self, path: str):
        logger.info("running")
        path = Path(path).absolute()

        files = (p.resolve() for p in Path(path).glob("**/*")
              n   if p.suffix in {".jpg", ".jpeg", ".png"})

        for image_path in tqdm(files):
            logger.info(f"Sending image: {image_path.as_posix()}")
            img, new_size_ratio, original_size, new_size = compress_img(
                image_path.as_posix())
            _, buffer = cv2.imencode(".jpg", np.array(img))
            base64_image = b64encode(buffer.tobytes())
            msg = BuildMessage(file_path=image_path.as_posix(),
                               original_size=original_size,
                               new_size_ratio=new_size_ratio,
                               new_size=new_size,
                               b64_image=base64_image)

            self.messageQueue.send(str(msg))
            time.sleep(0.1)
            logger.info("Image sent")


if __name__ == "__main__":
    rp = Producer()
    rp.run(
        "/Users/arm/Code/Projects/Freelance/TTH/FaceRecognitionTTHKnitting/Runner/"
    )
