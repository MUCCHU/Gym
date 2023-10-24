from rest_framework import serializers
from .models import Gym, Trainer, Client, WorkoutSession


class GymSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    address = serializers.CharField()

    def create(self, validated_data):
        return Gym.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
    
class TrainerSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    specialization = serializers.CharField(max_length=100)
    gym = serializers.PrimaryKeyRelatedField(queryset=Gym.objects.all())

    def create(self, validated_data):
        return Trainer.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.specialization = validated_data.get('specialization', instance.specialization)
        instance.gym = validated_data.get('gym', instance.gym)
        instance.save()
        return instance
    
class ClientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

    def create(self, validated_data):
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance
    
class WorkoutSessionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    trainer = serializers.PrimaryKeyRelatedField(queryset=Trainer.objects.all())
    date = serializers.DateField()
    duration = serializers.IntegerField()

    def create(self, validated_data):
        return WorkoutSession.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.client = validated_data.get('client', instance.client)
        instance.trainer = validated_data.get('trainer', instance.trainer)
        instance.date = validated_data.get('date', instance.date)
        instance.duration = validated_data.get('duration', instance.duration)
        instance.save()
        return instance