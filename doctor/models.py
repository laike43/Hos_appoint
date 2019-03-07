from django.db import models

# Create your models here.


class Doctor(models.Model):
    '''
    医生用户表
    '''
    gender = (
        ('male','男'),
        ('female','女')
              )
    num = models.CharField(max_length=100)
    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=12)
    department = models.CharField(max_length=200)
    message = models.TextField()
    infirmary = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Seats(models.Model):
    name = models.CharField(max_length=120)
    seat_num = models.CharField(max_length=100)
    starttime = models.DateTimeField()
    endtime = models.DateTimeField()
    brief = models.TextField(max_length=300)
    seatsnum = models.IntegerField(default=0)
    def __str__(self):
        return self.name

