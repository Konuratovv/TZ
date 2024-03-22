from django.contrib import admin
from django.urls import path
from .views import CreateAppartmentAPIView, UpdateAppartmentAPIView, DeleteAppartmentAPIView, ListAppartmentsAPIView

urlpatterns = [
    path('add-appartment/', CreateAppartmentAPIView.as_view()),
    path('update/<int:pk>/appartment/', UpdateAppartmentAPIView.as_view()),
    path('delete/<int:pk>/appartment/', DeleteAppartmentAPIView.as_view()),
    path('appartments/', ListAppartmentsAPIView.as_view())
]
