from celery import Celery
import Config as ENV

app = Celery(

    'lodashai',
    broker=ENV.RABBITMQ_BROKER,
    backend=ENV.REDIS_HOST_URL,
    include=[
        'engine.service.Prepare',

    ]
)

app.conf.update(
    enable_utc=True,
    timezone='Asia/Bangkok',
    task_serializer='json',
    result_serializer='json',
    result_expires=60000,

)
