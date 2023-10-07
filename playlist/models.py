from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, User

# Create your models here.

class CustomUserManager(BaseUserManager):

    def create_user(self, password=None, **extra_fields):
        user = self.model(**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'


class Collection(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    genres = models.CharField(max_length=255, blank=True)
    uuid = models.CharField(max_length=36)
    collection = models.ForeignKey(Collection, related_name='movies', on_delete=models.CASCADE)


class RequestCount(models.Model):
    count = models.IntegerField(default=0)