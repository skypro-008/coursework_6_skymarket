from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    '''Команда для создания пользователя с ролью - admin'''

    def handle(self, *args, **options):
        # Staff
        user = User.objects.create(
            email='kolya@mail.ru',
            username='nikolai',
            first_name='Nikolai',
            last_name='Petrov',
            phone=None,
            role='admin',
            is_active=True,

        )
        user.set_password('121test121')
        user.save()
