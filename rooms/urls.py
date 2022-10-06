from rest_framework.routers import DefaultRouter
from . import views 

router = DefaultRouter() 
router.register('rooms', views.RoomViewSet, basename='rooms')

urlpatterns = router.urls