from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("/blog", views.blog, name="blog"),
    path("/cart", views.cart, name="cart"),
    path("/category", views.category, name="category"),
    path("/checkout", views.checkout, name="checkout"),
    path("/confirmation", views.confirmation, name="confirmation"),
    path("/contact", views.contact, name="contact"),
    path("/single-blog", views.singleblog, name="single-blog"),
    path("/single-product", views.singleproduct, name="single-product"),
    path("/tracking", views.tracking, name="tracking"),
]
