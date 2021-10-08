
from json import encoder
from engine.model import FaceLocalizer, FaceExtractor
from celery import Task
from celery import group
from celery.utils.log import get_task_logger
from Worker import app
import cv2
from PIL import Image
from engine.utils.log import Logger
celery_log = get_task_logger(__name__)


class FacePrepareModel(Task):
    """
    Abstraction of Celery's Task class to support loading ML model.
    """
    abstract = True

    def __init__(self):
        super().__init__()
        self.model_list = {}

    def __call__(self, *args, **kwargs):
        """
        Load model on first call (i.e. first task processed)
        Avoids the need to load model on each task request
        """
        # MessageLogger.Warn_print(self)

        if len(self.model_list) < 1:
            celery_log.info('Loading Model...')

            FaceLocalizerModel = FaceLocalizer(margin=5)

            self.model_list.update(
                {"FaceLocalizer": FaceLocalizerModel})

            celery_log.info('Model Loaded Success')

        return self.run(*args, **kwargs)


@app.task(
    name="prepareface",
    ignore_result=False,
    bind=True,
    trail=True,
    base=FacePrepareModel,
    autoretry_for=(Exception,),
    retry_kwargs={'max_retries': 3, 'countdown': 10},
    retry_jitter=False
)
def FaceDetection(self, image_path):
    result = {}
    group_faces = []

    image = cv2.imread(image_path)

    faces = self.model_list['FaceLocalizer'].detect_faces(image)

    result["result"] = faces
    result["message"] = f"Founded {len(faces)} faces" if len(
        faces) > 0 else "Not Founded Faces"

    if len(faces) > 0:
        for i, _ in enumerate(faces):
            __face = faces[i]
            group_faces.append(FaceEncoding.s(image_path, i, __face))

        task = group(group_faces).apply_async()

    return task


class FaceEncoding(Task):
    """
    Abstraction of Celery's Task class to support loading ML model.
    """
    abstract = True

    def __init__(self):
        super().__init__()
        self.model_list = {}

    def __call__(self, *args, **kwargs):
        """
        Load model on first call (i.e. first task processed)
        Avoids the need to load model on each task request
        """
        # MessageLogger.Warn_print(self)

        if len(self.model_list) < 1:
            celery_log.info('Loading Model...')

            FaceExtractorModel = FaceExtractor(margin=5)

            self.model_list.update(
                {"FaceExtractor": FaceExtractorModel})

            celery_log.info('Model Loaded Success')

        return self.run(*args, **kwargs)


@app.task(
    name="alignface",
    ignore_result=False,
    bind=True,
    trail=True,
    base=FaceEncoding,
    autoretry_for=(Exception,),
    retry_kwargs={'max_retries': 3, 'countdown': 10},
    retry_jitter=False
)
def FaceEncoding(self, image_path, id, face_cord):

    encoded_face = self.model_list['FaceExtractor'].extractFeature(
        image_path, id, face_cord)
