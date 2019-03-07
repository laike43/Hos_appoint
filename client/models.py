from django.db import models
from doctor.models import Seats
# Create your models here.
class Patient(models.Model):
    gender = (
        ('male', '男'),
        ('female', '女')
    )
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=12)
    message = models.TextField()
    brief = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Appointment(models.Model):
    client_name = models.CharField(max_length=120)
    doctor_name = models.CharField(max_length=120)
    seat_num = models.CharField(max_length=100)
    client_message = models.TextField()
    doc_message = models.TextField()
    agree = models.BooleanField(default=False,null=True)
    def __str__(self):
        return self.client_name
