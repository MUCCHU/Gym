from django.contrib import admin
from .models import Gym, Trainer, Client, WorkoutSession
# Register your models here.

admin.site.register(Gym)
admin.site.register(Trainer)
admin.site.register(Client)
admin.site.register(WorkoutSession)