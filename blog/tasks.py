import string
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from blog.models import Post
from celery import shared_task


@shared_task
def create_random_posts(amount):
    for i in range(amount):
        random_string = get_random_string(10, string.ascii_letters)
        title = f'Random_{random_string}'
        text = get_random_string(200)
        author = User.objects.get(pk=1)
        post = Post.objects.create(author=author, title=title, text=text)
        post.publish()
