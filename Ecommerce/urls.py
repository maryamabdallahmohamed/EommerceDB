from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name="home"),
    path('about/', views.about , name="about"),
    path('contact/', views.contact , name="contact"),
    path('products/', views.products , name="products"),
    path('single_product/', views.single_product , name="single_product"),
    path('mens/', views.mens , name="mens"),
    path('womens/', views.womens , name="womens"),
    path('kids/', views.kids , name="kids"),
    path('cart/', views.cart , name="cart")
]