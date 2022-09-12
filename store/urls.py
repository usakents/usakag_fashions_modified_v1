from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

    path('bags/', views.manage_bags, name="bags"),
    path('men/', views.manage_men, name="men"),
    path('scarves/', views.manage_scarves, name="scarves"),
    path('women/', views.manage_women, name="women"),
    path('special_offers/', views.manage_special_offers, name="special_offers"),
    path('single_product/<int:productId>/',views.single_product,name='single_product'),
    path('about_us/', views.manage_about_us, name="about_us"),
    path('faq/', views.manage_faq, name="faq"),
    
    path("register", views.register, name= "register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name= "logout"),


]