from celery import Celery
from celery.schedules import crontab
import os

redis_pwd = os.getenv('REDIS_PWD')
app = Celery('tasks', broker=f'redis://:{redis_pwd}@redis:6379/0', backend=f'redis://:{redis_pwd}@redis:6379/0')

@app.task
def insert_data_to_redis_task():
    print("success")

app.conf.beat_schedule = {
    'insert-data-every-5-minutes': {
        'task': 'app.tasks.insert_data_to_redis_task',
        'schedule': crontab(hour=3, minute=0),
        'args': (),
    }
}