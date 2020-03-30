from django.db import models
import uuid
from django.contrib.auth.models import User
import datetime
#from django.contrib.gis.geos import GEOSGeometry
#from django.contrib.gis.geos import Point
from django.conf import settings
import uuid  # The uuid module
# Create your models here.

def generate_test_id():
    return str(uuid.uuid4()).split("-")[-1] #generate unique ticket id

class Appointment(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL,blank=True, null=True,on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #test_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # using the function uuid4 on the module
    #test_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    #test_id = models.CharField(max_length=2000, blank=True, default='COV19')
    code = models.CharField(max_length=2000, blank=True, default='')

    def save(self, force_insert=False, force_update=False):
        if self.code == "":
            existing_codes = Appointment.objects.all().order_by('-code')
            if existing_codes.count() > 0:
                new_code = int(existing_codes[0].code[1:]) + 1
            else:
                new_code = 0
            self.code = 'COV%03d' % new_code
        super(Appointment, self).save(force_insert, force_update)


    appointment_date = models.DateField(blank=True)
    appointment_date = models.TimeField(blank=True)
    first_name = models.CharField(max_length=50)
    middle_Name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    dob = models.DateField()
    sex = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    lga = models.CharField(max_length=50)
    ward = models.CharField(max_length=50)
    polling_unit = models.CharField(max_length=50)
	#geolocation = models.EOSGeometry('POINT(LON LAT)', srid=4326)
    ##geolocation = Point(1, 1)
    prepared_state_of_testing = models.CharField(max_length=50)
    phone_numbr = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


    def __unicode__(self):
        return self.code

    def __str__(self):
        return self.code

    # def __str__(self):

    #     return "{} - {}".format(self.first_name, self.test_id)

    # def save(self, *args, **kwargs):
    #     if len(self.code.strip(" "))==0:self.appointment_id = generate_test_id()

    #     super(Appointment, self).save(*args, **kwargs) # Call the real   save() method

    class Meta:
        ordering = ["-appointment_date"]


