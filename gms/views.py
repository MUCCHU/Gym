from django.shortcuts import render
from rest_framework import viewsets
from .models import Gym, Trainer, Client, WorkoutSession
from .serializers import GymSerializer, TrainerSerializer, ClientSerializer, WorkoutSessionSerializer
# Create your views here.
class GymViewSet(viewsets.ModelViewSet):
    serializer_class = GymSerializer
    queryset = Gym.objects.all()
    # def list(self, request):
    #     pass

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass

class TrainerViewSet(viewsets.ModelViewSet):
    serializer_class = TrainerSerializer
    queryset = Trainer.objects.all()

class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class WorkoutSessionViewSet(viewsets.ModelViewSet):
    serializer_class = WorkoutSessionSerializer
    queryset = WorkoutSession.objects.all()

