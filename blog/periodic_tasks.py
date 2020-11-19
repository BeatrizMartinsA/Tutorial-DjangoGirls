from celery import shared_task
from django.core.management import call_command
from blog.celery import app
from celery.schedules import crontab


@shared_task
def p_create_random_posts():
    call_command('create_random_posts')


def schedule():
   app.add_periodic_task(crontab(), p_create_random_posts.s())