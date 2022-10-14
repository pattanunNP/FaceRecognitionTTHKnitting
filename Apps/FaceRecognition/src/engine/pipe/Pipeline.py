from logging import log
from engine.service.Prepare import FaceDetection
import os
from engine.utils.log import Logger
from engine.utils.is_image_file import is_image_file
from tqdm.auto import tqdm

logger = Logger(name="Pipeline", level="info",
                log_file="../run.log", save_to_file=True)


class Pipeline:

    def __init__(self) -> None:

        logger.info("Initializing Pipeline")
        logger.info("Initializing Pipeline OK")

    def PrepareImage(self, dir):
        total_image = 0
        images_list = []
        logger.info(f"[Checking] Data Directory at {dir}")

        if os.path.isdir(dir):
            logger.info(f"[Checking] Data Directory at {dir} OK")
            logger.info(f"Founded {len(os.listdir(dir))} folders")

            for path, _, files in os.walk(dir):
                for file in filter(is_image_file, files):
                    image_path = os.path.join(path, file)
                    total_image += 1
                    images_list.append(image_path)

            logger.info(f"Founded total {total_image} images")
            for image_path in tqdm(images_list):
                logger.info(f"Processing: {image_path}")

                task = FaceDetection.s(image_path)

                task = task.apply_async()

                logger.info(f"Accepted Task : {task.id}")

        else:
            logger.warn(
                f"[Checking] Data Directory at {dir} Not exits")