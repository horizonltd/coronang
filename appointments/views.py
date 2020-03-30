from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from appointments.serializers import UserSerializer, AppointmentSerializer
from django.contrib.auth.models import User
from appointments.models import Appointment, User

# Create your views here.

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# ViewSets define the view behavior.
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
