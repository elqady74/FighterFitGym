from rest_framework import serializers
from .models import GymUser, Trainer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GymUser
        fields = ['user_id', 'fname', 'lname', 'email', 'password_hash', 'phone', 'role', 'height', 'weight']
        extra_kwargs = {'password_hash': {'write_only': True}}

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['trainer_id', 'specialization', 'hourly_rate', 'certification', 'bio']