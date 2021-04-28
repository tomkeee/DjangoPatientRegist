from django.db import models
from django.contrib.auth.models import User
from doctor.models import Doctor
from django.contrib.auth import get_user_model

# Create your models here.

User=get_user_model()
class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    doctor= models.ForeignKey(Doctor,on_delete=models.CASCADE)
    check_in=models.DateTimeField()
    check_out=models.DateTimeField()
    
    def __str__(self):
        return f"{self.user} has made an appointment from {self.check_in}"
