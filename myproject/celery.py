# import os

# from celery import Celery
# import webbrowser
# from time import sleep


# # Set the default Django settings module for the 'celery' program.
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# app = Celery('myproject')

# # Using a string here means the worker doesn't have to serialize
# # the configuration object to child processes.
# # - namespace='CELERY' means all celery-related configuration keys
# #   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Load task modules from all registered Django apps.
# app.autodiscover_tasks()



# @app.task(bind=True)
# def debug_task(self):
#     print("HELLO Pankaj!!!!!!")
# @app.task(bind=True)
# def debug(self):
#     print("HELLO pk!!!!!!")

# @app.task(bind=True)
# def mytk(self):
#     url = 'http://127.0.0.1:8000/schedulepinstimes/'

#     while True:
#         print("refreshing...")
#         webbrowser.open(url, new=0)
#         sleep(25)



# @app.task(bind=True)
# def per(self):
#     url = 'http://127.0.0.1:8000/giveaccesstotempuser/?mobile=9170399004&f_id=7896304'

#     # while True:
#     #     print("refreshing...")
#     webbrowser.open(url, new=0)
#     sleep(5)
# ##http://127.0.0.1:8000/tempuserautodelete/
# ##
# @app.task(bind=True)
# def tempuserautodelete(self):
#     url = 'http://127.0.0.1:8000/tempuserautodelete12/'

#     # while True:
#     #     print("refreshing...")
#     webbrowser.open(url, new=0)
#     sleep(5)
# @app.task(bind=True)
# def threeyearstask(self):
#     url = 'http://127.0.0.1:8000/schedulebillpredictionyear/'

#     # while True:
#     #     print("refreshing...")
#     webbrowser.open(url, new=0)
#     sleep(5)

# @app.task(bind=True)
# def debug_task(self):
#     print(f'Request: {self.request!r}')

# Commands for Celery

########  Schedule the tasks than run these commands  #########

# 1. celery -A myproject beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
# 2. celery -A myproject worker -l INFO
# 3. python3 manage.py runserver
import os
from celery import Celery
from datetime import timedelta
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')
app = Celery('myproject')
app.config_from_object('django.conf:settings', namespace='CELERY')
 
app.conf.timezone = 'Asia/Kolkata'
 
app.conf.beat_schedule = {
    "every_thirty_seconds": {
        "task": "myapp.tasks.thirty_second_func",
        "schedule": timedelta(seconds=10),
    },
}
 
app.autodiscover_tasks()