from django.db import models
from datetime  import datetime, time
from django.contrib.auth.models import User
from doctor.models import Doctor
from django.contrib.auth import get_user_model

# Create your models here.

User=get_user_model()
class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    doctor= models.ForeignKey(Doctor,on_delete=models.CASCADE)
    check_in_date=models.DateTimeField(auto_now=False, auto_now_add=False,)
    check_out_date=models.DateTimeField(auto_now=False, auto_now_add=False,)
    
    def __str__(self):
        return f"{self.user} has made an appointment with {self.doctor} from {self.check_in_date}"