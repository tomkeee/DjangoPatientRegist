from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Patient(models.Model):
    first_name   = models.CharField(max_length=20,default="Tomek")
    last_name    =models.CharField(max_length=30,default="Tomek")
    street       =models.CharField(max_length=30,default="Tomek")
    city         =models.CharField(max_length=30,default="Tomek")
    number       =models.PositiveIntegerField(default=12)
    phone_number =models.CharField(max_length=30,default=12)

    def get_absolute_url(self):
        return reverse("patient-detail",kwargs={"id":self.id})