from django.contrib import admin
from django.urls import path, include

from django.contrib.auth.models import User
from appointments.models import Appointment
from rest_framework import routers
from appointments.views import UserViewSet, AppointmentViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api/users', UserViewSet)

router.register(r'api/appointment', AppointmentViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),    
    path(r'', include(router.urls)),
    path(r'api/', include('rest_framework.urls', namespace='rest_framework'))

]