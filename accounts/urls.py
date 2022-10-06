from rest_framework.authtoken import views as views_auth
from rest_framework.routers import DefaultRouter

from django.urls import path
from . import views 

router = DefaultRouter() 
router.register('users', views.UserViewSet, basename='users')


urlpatterns = [
    path('api-token-auth/', views_auth.obtain_auth_token)
]




urlpatterns += router.urls