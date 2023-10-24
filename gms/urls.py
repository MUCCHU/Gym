from django.urls import path
from rest_framework import routers
from .views import GymViewSet, TrainerViewSet, ClientViewSet, WorkoutSessionViewSet

router = routers.DefaultRouter()

router.register('gyms', GymViewSet)
router.register('trainers', TrainerViewSet)
router.register('clients', ClientViewSet)
router.register('workout_sessions', WorkoutSessionViewSet)

