from rest_framework import serializers
from django.contrib.auth.models import User  # Or use your custom User model
from .models import Profile  # Assuming you have a Profile model

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['user', 'bio', 'avatar']  # Add other profile fields as needed

