from rest_framework import serializers

from django.contrib.auth.models import User
from appointments.models import Appointment

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# Serializers define the API representation.
class AppointmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Appointment
        fields = ('__all__')
        depth=1