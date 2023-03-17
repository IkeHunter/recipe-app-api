"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


class UserManager(BaseUserManager):
    """Manager for users."""

    # make sure it's spelled correctly! other components use this
    def create_user(self, email, password=None, **extra_fields):
        """Create, save, return new user."""
        if not email:
            # built in error, no import
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)  # save user to db

        return user

    def create_superuser(self, email, password):
        """Create and return new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


# ABU base for auth but not fields, PM contains permissions and fields
class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    # determines if they can log into django admin
    is_staff = models.BooleanField(default=False)

    objects = UserManager()  # assign user manager to custom user class

    USERNAME_FIELD = 'email'
