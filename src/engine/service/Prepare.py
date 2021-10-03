
from engine.model import FaceLocalizer
from celery import Task
from celery.utils.log import get_task_logger
from Worker import app

from engine.utils.log import Logger
celery_log = get_task_logger(__name__)


model = None


class FaceDetection(Task):
    """
    Abstraction of Celery's Task class to support loading ML model.
    """
    abstract = True

    def __init__(self):
        super().__init__()
        self.model = {}

    def __call__(self, *args, **kwargs):
        """
        Load model on first call (i.e. first task processed)
        Avoids the need to load model on each task request
        """
        # MessageLogger.Warn_print(self)

        celery_log.info('Loading Model...')
        # pprint(ServiceController.get_avaliable_service(
        #     type="FACE_ANALYSIS"), indent=4)

        self.model = FaceLocalizer(margin=5)

        return self.run(*args, **kwargs)


@app.task(
    name="train",
    ignore_result=False,
    bind=True,
    trail=True,
    base=FaceDetection,
    autoretry_for=(Exception,),
    retry_kwargs={'max_retries': 5, 'countdown': 2},
    retry_jitter=False
)
def FaceDetection(self, image):
    faces = self.model.detect_faces(image)
    return faces
