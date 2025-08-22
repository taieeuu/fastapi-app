from celery import Celery
from celery.schedules import crontab
import os
import logging
from datetime import timedelta
import logging

redis_pwd = os.getenv('REDIS_PWD')
logging.info(f"redis_pwd: {redis_pwd}")
app = Celery('tasks', broker=f'redis://:{redis_pwd}@redis:6379/0', backend=f'redis://:{redis_pwd}@redis:6379/0')

app.conf.enable_utc = False
app.conf.timezone = 'Asia/Taipei'
app.conf.result_expires = timedelta(days=365)

@app.task
def insert_data_to_redis_task():
    logging.info("success")

app.conf.beat_schedule = {
    'insert-data-every-5-minutes': {
        'task': 'app.tasks.insert_data_to_redis_task',
        'schedule': crontab(hour=3, minute=0),
        'args': (),
    }
}
