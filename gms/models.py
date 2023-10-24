from django.db import models


class Gym(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
class Trainer(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    gym = models.OneToOneField(Gym, on_delete=models.CASCADE, related_name='trainers')

    def __str__(self):
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name

class WorkoutSession(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='workout_sessions')
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, related_name='workout_sessions')
    date = models.DateField()
    duration = models.IntegerField()

    def __str__(self):
        return self.client.name + '\'s workout session'
