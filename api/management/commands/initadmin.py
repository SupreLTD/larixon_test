from environs import Env

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

env = Env()
env.read_env()


class Command(BaseCommand):

    def handle(self, *args, **options):
        username = env.str('DJANGO_SUPERUSER_USERNAME')
        email = env.str('DJANGO_SUPERUSER_EMAIL')
        password = env.str('DJANGO_SUPERUSER_PASSWORD')

        if not User.objects.filter(username=username).exists():
            print('Creating account for %s (%s)' % (username, email))
            admin = User.objects.create_superuser(
                email=email, username=username, password=password)
        else:
            print('Admin account has already been initialized.')
