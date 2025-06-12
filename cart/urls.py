from django.urls import path
from cart.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('detail/', cart_detail, name='cart'),
    path('add/<int:id>/', cart_add, name='cart_add'),
    path('delete_cart/<int:id>/', cart_remove, name='cart_remove'),
    path('order/', order, name='order'),
]