from typing import Optional
from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)


class UserManager(BaseUserManager):
    def __create_user(self, email, nickname=None, password=None):
        """avoid duplication"""
        if not email:
            raise ValueError("The Email field must be set! 💀")

        user = self.model(email=self.normalize_email(email), nickname=nickname)
        user.set_password(password)

        return user

    def create_user(self, email, nickname=None, password=None):
        """Create and save User with given parameters"""
        user = self.__create_user(email, nickname=nickname, password=password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, nickname=None, password=None):
        """Create and save Superuser with given parameters"""
        user = self.__create_user(email, nickname=nickname, password=password)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User Model"""

    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    nickname = models.CharField(max_length=255)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["nickname"]

    def __str__(self):
        return str(self.nickname)

    def has_perm(self, perm: str, obj=None) -> bool:
        return super().has_perm(perm, obj)

    def has_module_perms(self, app_label: str) -> bool:
        return super().has_module_perms(app_label)