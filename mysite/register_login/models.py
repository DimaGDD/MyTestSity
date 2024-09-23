from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.crypto import get_random_string


class CustomUserManager(BaseUserManager):
    def create_user(self, username=None, email=None, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set!')
        elif not username:
            raise ValueError('The Username field must be set!')
        elif not password:
            raise ValueError('The Password field must be set!')


        email = self.normalize_email(email)
        user_id = self.generate_user_id()

        user = self.model(email=email, username=username, id=user_id, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, email, password, **extra_fields)


    def generate_user_id(self):
        while True:
            user_id = get_random_string(length=6, allowed_chars='0123456789')
            if user_id[0] != 0:
                if not User.objects.filter(id=user_id).exists():
                    return user_id


def user_avatar_path(instance, filename):
    return f'{instance.email}/avatar/{filename}'


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True, blank=False)

    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    avatar = models.ImageField(upload_to=user_avatar_path, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email