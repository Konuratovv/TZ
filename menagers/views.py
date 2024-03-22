from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from menagers.models import Managers
from menagers.serializers import CreateManagersSerializer, UpdateManagerSerializer, DeleteManagerSerializer, LoginManagerSerializer
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken


class CreateManagersAPIView(generics.CreateAPIView):
    serializer_class = CreateManagersSerializer

    def post(self, request, *args, **kwargs):
        serializer = CreateManagersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        manager = serializer.create(serializer.validated_data)
        return Response({'status': 'Менеджер добавлен!'})
    
class LoginManagerAPIView(generics.CreateAPIView):
    serializer_class = LoginManagerSerializer
    permission_classes = [AllowAny]


    def post(self, request, *args, **kwargs):
        manager = Managers.objects.filter(email=self.request.data['email']).first()
        if manager is None:
            raise AuthenticationFailed('User not found')
        
        if not manager.check_password(self.request.data['password']):
            raise AuthenticationFailed('Incorrect password')
        
        access_token = AccessToken.for_user(manager)
        refresh_token = RefreshToken.for_user(manager)

        return Response({'access_token': str(access_token), 'refresh_token': str(refresh_token)})
    
class UpdateManagersAPIView(generics.UpdateAPIView):
    serializer_class = UpdateManagerSerializer

    def patch(self, request, *args, **kwargs):
        manager = Managers.objects.get(pk=self.request.data.get("manager_id"))
        manager.name = self.request.data.get('name')
        manager.phone_number = self.request.data.get('phone_number')
        manager.email = self.request.data.get('email')
        manager.save()
        return Response({'status': 'Менеджер обновлен!'})
    
class DeleteManagerAPIView(generics.DestroyAPIView):
    serializer_class = DeleteManagerSerializer
    queryset = Managers.objects.all()

class ListManagersAPIView(generics.ListAPIView):
    serializer_class = DeleteManagerSerializer
    queryset = Managers.objects.all()
