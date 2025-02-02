# Farm/urls.py
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
router.register('farms', FarmViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # Include the router's URLs
    path('api/breeds/by_type/<str:pk>/', BreedViewSet.as_view({'get': 'by_type'}), name='breeds-by-type'),
    path('api/animals/by_type_and_farm/', AnimalViewSet.as_view({'get': 'by_type_and_farm'}), name='animals-by-type-and-farm'),
    path('api/breeds/by_type_and_farm/', BreedViewSet.as_view({'get': 'by_type_and_farm'}),
         name='breeds-by-type-and-farm'),

]