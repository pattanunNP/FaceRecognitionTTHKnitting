from logguru import logger
import cv2


def delivery_report(err, msg):
    if err:
        logger.error("Failed to deliver message: {0}: {1}"
              .format(msg.value(), err.str()))
    else:
        logger.info(f"msg produced. \n"
                    f"Topic: {msg.topic()} \n" +
                    f"Partition: {msg.partition()} \n" +
                    f"Offset: {msg.offset()} \n" +
                    f"Timestamp: {msg.timestamp()} \n")
                    
def serializeImg(img):
    _, img_buffer_arr = cv2.imencode(".jpg", img)
    img_bytes = img_buffer_arr.tobytes()
    return img_bytes