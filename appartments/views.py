from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import CreateAppartmentsSerializer, UpdateAppartmentSerializer, DeleteApprtmentSerializer
from .models import Appartments
from django_filters.rest_framework import DjangoFilterBackend
from .filters import AppartmentFilter

# Create your views here.

class CreateAppartmentAPIView(generics.CreateAPIView):
    serializer_class = CreateAppartmentsSerializer

    def post(self, request, *args, **kwargs):
        serializer = CreateAppartmentsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        appartment = serializer.create(serializer.validated_data)
        return Response({'status': 'Квартира добавлена!'})
    

class UpdateAppartmentAPIView(generics.UpdateAPIView):
    serializer_class = UpdateAppartmentSerializer

    def patch(self, request, *args, **kwargs):
        appartment = Appartments.objects.get(pk=self.request.data.get('appartment_id'))
        appartment.customer = self.request.data.get('customer')
        appartment.customer_number = self.request.data.get('customer_number')
        appartment.contract_number = self.request.data.get('contract_number')
        appartment.status = self.request.data.get('status')
        appartment.save()
        return Response({'status': 'Изменения сохранены!'})
    
class DeleteAppartmentAPIView(generics.DestroyAPIView):
    serializer_class = DeleteApprtmentSerializer
    queryset = Appartments.objects.all()

class ListAppartmentsAPIView(generics.ListAPIView):
    serializer_class = DeleteApprtmentSerializer
    queryset = Appartments.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = AppartmentFilter

