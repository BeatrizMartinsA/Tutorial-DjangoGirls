from django.core.management.base import BaseCommand
from blog import tasks

class Command(BaseCommand):
    help='Cria 20 posts aleatórios'

    def handle(self, *args, **options):
        tasks.create_random_posts.delay(20)
