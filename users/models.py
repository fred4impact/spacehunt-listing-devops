from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import os

def user_directory_path(instance, filename):
    # Get the user's ID or any other unique identifier
    user_id = instance.user.id
    # Build the upload path using the user's ID and the filename
    # The final path will be 'uploads/user_<id>/<filename>'
    return f'uploads/user_{user_id}/{filename}'




class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
        email = models.EmailField(unique=True)
        first_name = models.CharField(max_length=50)
        last_name = models.CharField(max_length=50)
        created_at = models.DateTimeField(default=timezone.now)

        is_realtor = models.BooleanField(default=False)
        is_staff = models.BooleanField(default=False)

        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = ['first_name', 'last_name']

        objects = UserManager()

        def __str__(self):
            return self.email



class Realtor(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='realtor')
        profile = models.TextField()
        photo = models.ImageField(upload_to= user_directory_path, blank=True, null=True)
        
        agency = models.CharField(max_length=100, blank=True, null=True)
        agent_id_num = models.CharField(max_length=50)
        agent_id_card =models.ImageField(upload_to='agent_vcard/', blank=True)

        contact_number=models.CharField(max_length=20) 
        city = models.CharField(max_length=100, blank=True)
        country = models.CharField(max_length=100, blank=True)

        is_active = models.BooleanField(default=False)

    
        def toggle_activation(self):
            if not self.user.is_superuser:
                raise PermissionDenied("Only superuser can activate realtors.")

            self.is_active = True
            self.save()

        def save(self, *args, **kwargs):
            super().save(*args, **kwargs)

            if self.is_profile_complete() and not self.is_active:
                self.toggle_activation()

        def is_profile_complete(self):
            # Add your logic to check if the realtor profile is complete
            # Return True if the profile is complete, False otherwise
            # For example, you can check if all required fields are filled

            # Example code to check if all required fields are filled
            required_fields = ['profile', 'photo', 'agency', 'agent_id_num', 'contact_number', 'city', 'country']
            return all(getattr(self, field) for field in required_fields)


        def __str__(self):
             return self.user.email

     