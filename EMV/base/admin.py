from django.contrib import admin
from .models import Product, Vendor
# Register your models here.
admin.site.register([Product, Vendor])