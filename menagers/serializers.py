from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from rest_framework.validators import UniqueValidator

from menagers.models import Managers

class CreateManagersSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    email = serializers.CharField(write_only=True, validators=[UniqueValidator(queryset=Managers.objects.all())])

    class Meta:
        model = Managers
        fields = ['name', 'phone_number', 'email', 'password']

class LoginManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Managers
        fields = [
            'email',
            'password',
        ]

class UpdateManagerSerializer(serializers.ModelSerializer):
    email = serializers.CharField(write_only=True, validators=[UniqueValidator(queryset=Managers.objects.all())])

    class Meta:
        model = Managers
        fields = ['name', 'phone_number', 'email']

class DeleteManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Managers
        fields = '__all__'