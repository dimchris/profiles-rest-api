from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from typing import List

class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""
    
    def create_user(self, email:str, name:str, password:None) -> 'UserProfile':
        """Create a new user profile"""
        if not email:
            raise ValueError('Users must have an email address')
        
        email = self.normalize_email(email=email)
        user:'UserProfile' = self.model(email=email, name =name)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user;
    
    def create_superuser(self, email:str, name:str, password:str) -> 'UserProfile':
        """Create and save a new super user with given details"""
        user:'UserProfile' = self.create_user(email=email, name=name, password=password)
        
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ Database model for  users in the sysetem """
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default = True)
    
    objects = UserProfileManager()
    
    USERNAME_FIELD:str = 'email'
    REQUIRED_FIELDS:List[str] = ['name']
    
    def get_full_name(self) -> str:
        """Retrieve full name of user"""
        return self.name
    
    def get_short_name(self) -> str:
        """Return short name of user"""
        return self.name
    
    def __str__(self) -> str:
        """Return string representation of user"""
        return self.email