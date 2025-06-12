from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.SimpleRouter()
router.register(r"admins", admins_api)

urlpatterns = [
    path('', main_pg, name='mainpage'),
    path('category/<int:id>/', category_pg, name='categorypage'),
    path('brand/<int:id>/', brand_pg, name='brandpage'),
    path('detail/<int:id>/', detail_pg, name='detailpage'),
    path('administration/', admin_pg, name='adminpage'),
    path('api/', include(router.urls)),
]
