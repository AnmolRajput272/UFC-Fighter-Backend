from rest_framework import serializers
from django.contrib.auth.models import User
from django.db.models import Q

class user_register_serializer(serializers.Serializer):
    username = serializers.CharField(required=True, allow_blank=False)
    email = serializers.EmailField(required=True, allow_blank=False)
    password = serializers.CharField(required=True, allow_blank=False)

    def validate(self, data):
        if User.objects.filter(email = data['email']).exists():
            raise serializers.ValidationError("Email is already registered.")
        return data
    
    def create(self, validated_data):
        user = (
            User.objects.create_user(
                username = validated_data['username'],
                email = validated_data['email'],
                password = validated_data['password']
            )
        )
        return validated_data


class user_login_serializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()