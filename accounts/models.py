from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone

#from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    username = models.CharField(
        max_length=255,
    )
    # имеет ли пользователь доступ к интерфейсу администратора.
    is_staff = models.BooleanField(default=False)
    # активный аккаунт или нет
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    # Сообщает Django, что класс UserManager, определенный выше,
    # должен управлять объектами этого типа.
    objects = UserManager()

    USERNAME_FIELD = 'email'

    # все обязательные поля кроме поля имени пользователя и пароля,
    # поскольку эти поля всегда будут запрашиваться.
    # REQUIRED_FIELDS = ['username']

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

