from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register([Customer, Product, CartProduct, Cart,
                    Category, Order, Admin, ProductImage])
