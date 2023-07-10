from django.contrib.auth.models import AbstractUser
from django.db import models

GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
)

CHOICES = (
    ('bikes', 'Bikes'),
    ('electronics', 'Electronics'),
    ('books', 'Books'),
    ('sports', 'Sports'),
    ('cars', 'Cars'),
    ('commercial vehicles', 'Commercial Vehicles'),
)

STATE_CHOICES = (
    ('Andaman & Nicobar Islands', 'Andaman & Nicobar Islands'),
    ('Andra Pradesh', 'Andra Pradesh'),
    ('Arunachal Pradesh', 'Arunachal Pradesh'),
    ('Assam', 'Assam'),
    ('Bihar', 'Bihar'),
    ('Chhattisgarh', 'Chhattisgarh'),
    ('Chandigarh', 'Chandigarh'),
    ('Dadra & Nagar Haveli', 'Dadra & Nagar Haveli'),
    ('Delhi', 'Delhi'),
    ('Madhya Pradesh', 'Madhya Pradesh'),
    ('Uttar Pradesh', 'Uttar Pradesh'),
    ('Andra Pradesh', 'Andra Pradesh'),
    ('Mumbai', 'Mumbai'),
    ('Mizoram', 'Mizoram'),
    ('Nagaland', 'Nagaland'),
)

class User(AbstractUser):
    email = models.EmailField(max_length=254)
    wish_list = models.CharField(max_length=100, choices=CHOICES)
    gender = models.CharField(max_length=50, choices=GENDER)
    is_verified = models.BooleanField(default=False)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    address = models.CharField(max_length=50)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )






