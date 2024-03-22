from rest_framework import serializers
from .models import Object, Appartments

class ObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Object
        fields = '__all__'

class CreateAppartmentsSerializer(serializers.ModelSerializer):
    object = ObjectSerializer()

    class Meta:
        model = Appartments
        fields = [
            'object',
            'floor',
            'kv',
            'status',
            'price',
            'customer',
            'end_time',
        ]

class UpdateAppartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appartments
        fields = [
            'customer',
            'customer_number',
            'contract_number',
            'status',
        ]

class DeleteApprtmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appartments
        fields = '__all__'