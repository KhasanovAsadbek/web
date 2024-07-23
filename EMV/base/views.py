from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegisterForm, VendorProfileForm, ProductForm
from .models import Vendor, Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def index(request):
    featured_products = Product.objects.all()[:6]  # Get the first 6 products
    vendors = Vendor.objects.all()  # Get all vendors

    context = {
        'featured_products': featured_products,
        'vendors': vendors,
    }
    
    return render(request, 'index.html', context)

def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = VendorProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            vendor = profile_form.save(commit=False)
            vendor.user = user
            vendor.save()
            login(request, user)
            return redirect('profile')
    else:
        user_form = UserRegisterForm()
        profile_form = VendorProfileForm()
    return render(request, 'register.html', {'user_form': user_form, 'profile_form': profile_form})


@login_required
def profile(request):
    vendor = get_object_or_404(Vendor, user=request.user)
    return render(request, 'profile.html', {'vendor': vendor})

@login_required
def upload_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = Vendor.objects.get(user=request.user)
            product.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'upload_product.html', {'form': form})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})
