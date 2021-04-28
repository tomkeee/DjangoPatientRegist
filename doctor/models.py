from django.db import models

# Create your models here.
class Doctor(models.Model):
    TITLE_CATEGORIES= (
        ('PhD','PhD Student'),
        ('PD','Postdoctoral'),
        ('HbD','Habilitated doctor'),
        ('Prof','Professor')
    )
    first_name   = models.CharField(max_length=20)
    last_name    =models.CharField(max_length=30)
    street       =models.CharField(max_length=30)
    city         =models.CharField(max_length=30)
    number       =models.PositiveIntegerField(default=100)
    phone_number =models.CharField(max_length=30)
    title = models.CharField(max_length=4,choices=TITLE_CATEGORIES)
    price_for_visit = models.PositiveIntegerField(default=100)