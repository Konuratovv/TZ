from django.contrib import admin
from django.urls import path
from .views import CreateManagersAPIView, UpdateManagersAPIView, DeleteManagerAPIView, LoginManagerAPIView, ListManagersAPIView

urlpatterns = [
    path('add-manager/', CreateManagersAPIView.as_view()),
    path('update/<int:pk>/manager/', UpdateManagersAPIView.as_view()),
    path('delete/<int:pk>/manager/', DeleteManagerAPIView.as_view()),
    path('login-manager/', LoginManagerAPIView.as_view()),
    path('managers/', ListManagersAPIView.as_view())
]
