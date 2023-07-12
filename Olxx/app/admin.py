from django.contrib import admin
from .models import User,Product,Cart,OrderPlaced
# Register your models here.


@admin.register((User))
class UserModelAdmin(admin.ModelAdmin):
    list_display=['id','username','first_name','last_name','email','wish_list','gender','is_verified','locality','state','zipcode','address','password','last_login','is_superuser','is_staff','is_active','date_joined']

@admin.register((Product))
class ProductModelAdmin(admin.ModelAdmin):
    
    list_display=['id','title','selling_price','discounted_price','description','brand','category','product_image']

@admin.register((Cart))
class Cart(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

@admin.register((OrderPlaced))
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity','ordered_date','status']