from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Custom behavior: hash the password before saving
        user = Client.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
