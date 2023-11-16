from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Admin
        user = User.objects.create(
            email='svetars2015@yandex.ru',
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

        user.set_password('123star456')
        user.save()
