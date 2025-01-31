from django.urls import path, include
from rest_framework import routers

from .views import AnimalViewSet, BreedViewSet, TypeViewSet, StaffViewSet, EventViewSet, TaskViewSet, FarmViewSet

router = routers.DefaultRouter()
router.register('animals', AnimalViewSet)
router.register('breeds', BreedViewSet)
router.register('types', TypeViewSet)
router.register('staff', StaffViewSet)
router.register('events', EventViewSet)
router.register('tasks', TaskViewSet)
router.register(r'farms', FarmViewSet)


urlpatterns = [
    path('api/', include(router.urls)),  # Include the router's URLs
]