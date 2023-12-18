from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class UserRole(models.TextChoices):
    USER = 'user'
    ADMIN = 'admin'


class UserManager(BaseUserManager):
    '''
    Функция создания пользователя (user) — в нее мы передаем обязательные поля.
    raw_password - позволяет сделать пароль зашифрованным (необходимо для получения JWT Token)
    '''

    def create_user(self, email, first_name, last_name, phone, password=None, role='user'):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            role=role
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, password=None, role='admin'):
        '''
        Функция для создания суперпользователя — с ее помощью мы создаем админинстратора (admin).
        Это можно сделать с помощью команды - createsuperuser.
        '''

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            password=password,
            role=role
        )

        user.save(using=self._db)
        return user
