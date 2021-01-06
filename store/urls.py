from django.urls import path
from . import views

urlpatterns = [
    path('',views.store,name="main"),
    path('cart/',views.cart,name="cart"),
    path('checkout/',views.checkout,name="checkout"),
    path('store/',views.store,name="store"),
    path('update_item/', views.updateItem, name="update_item"),
    path('checkout_infos/',views.checkoutinfos,name="checkout_infos"),
    path('contact/',views.contact,name="contact")



]