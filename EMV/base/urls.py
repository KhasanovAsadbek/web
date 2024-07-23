from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('upload-product/', views.upload_product, name='upload_product'),
    path('product-list/', views.product_list, name='product_list'),
    path('login/', views.user_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]
