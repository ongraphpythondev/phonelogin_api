from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
from .managers import UserManager

class User(AbstractUser):
    username = None
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = UserManager()

    phone = PhoneField(unique=True, null=False, blank=True, help_text='Contact phone number')

    def __str__(self):
        return self.email
