import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestao_rh.settings')

app = Celery('gestao_rh')


app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()



@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')