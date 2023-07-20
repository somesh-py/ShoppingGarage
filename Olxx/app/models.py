from django.contrib.auth.models import AbstractUser
from django.db import models
from .manager import CustomManager

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

    username=None

    email = models.EmailField(max_length=254,unique=True)
    gender = models.CharField(max_length=50, choices=GENDER)
    is_verified = models.BooleanField(default=False)
    locality=models.CharField(max_length=50)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    zipcode=models.IntegerField(null=True)
    address = models.CharField(max_length=50)
    otp=models.CharField(max_length=5)

    USERNAME_FIELD='email'

    objects=CustomManager()

    REQUIRED_FIELDS=[]

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

CATEGORY_CHOICES =(
    ('B', 'Bikes'),
    ('EA','Electronics & Appliances'),
    ('BKS','Books'),
    ('S', 'Sports'),
    ('C', 'Cars'),
    ('CVS', 'Commercial Vehicles & Spares'),
) 

class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand = models.CharField(max_length=200)
    category = models.CharField(choices = CATEGORY_CHOICES,max_length=5)
    product_image = models.ImageField(upload_to='product_image')
    email=models.EmailField(max_length=254)

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

STAUS_CHOICES = (
    ('Accepted', 'Accepted'),
    ('packed','packed'),
    ('On The Way','On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel','Cancel')
)    

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default =1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length =50, choices = STAUS_CHOICES,default='Pending')