from loguru import logger
import cv2


def delivery_report(err, msg):
    if err:
        logger.error("Failed to deliver message: {0}"
              .format(err.str()))
    else:
        logger.info(f"msg produced. \n"
                    f"Topic: {msg.topic()} \n" +
                    f"Partition: {msg.partition()} \n" +
                    f"Offset: {msg.offset()} \n" +
                    f"Timestamp: {msg.timestamp()} \n")
                    
def serializeImg(img):
   
    return cv2.imencode(".jpg", img)[1].tobytes()