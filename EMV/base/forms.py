from django import forms
from django.contrib.auth.models import User
from .models import Vendor, Product

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class VendorProfileForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'address', 'phone_number', 'profile_picture', 'website']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'pdf_description']
