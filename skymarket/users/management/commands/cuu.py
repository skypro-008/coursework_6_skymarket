from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    '''Команда для создания пользователя с ролью - user'''

    def handle(self, *args, **options):
        # User
        user = User.objects.create(
            email='anna@mail.ru',
            username='anna',
            first_name='Anna',
            last_name='Sorokina',
            phone=None,
            role='user',
            is_active=True

        )
        user.set_password('111test222')
        user.save()
