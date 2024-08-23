from typing import List

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField, DateTimeField
from django.db.models.fields.related import ForeignKey
from profiles_project import settings


class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def create_user(self, email: str, name: str, password: None) -> "UserProfile":
        """Create a new user profile"""
        if not email:
            raise ValueError("Users must have an email address")

        email = self.normalize_email(email=email)
        user: "UserProfile" = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email: str, name: str, password: str) -> "UserProfile":
        """Create and save a new super user with given details"""
        user: "UserProfile" = self.create_user(
            email=email, name=name, password=password
        )

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for  users in the system"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)

    objects = UserProfileManager()

    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS: List[str] = ["name"]

    def get_full_name(self) -> str:
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self) -> str:
        """Return short name of user"""
        return self.name

    def __str__(self) -> str:
        """Return string representation of user"""
        return self.email


class ProfileFeedItem(models.Model):
    """Profile Status update"""

    user_profile = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
    )

    status_text = CharField(max_length=255)
    created_on = DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as string"""
        return self.status_text
