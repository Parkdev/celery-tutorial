import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True) #bind true는 self를 쓸수있냐 없냐
def debug_task(self):
    print('Request: {0!r}'.format(self.request))