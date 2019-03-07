from django.db import models


# Create your models here.
# 医院表
class Hospital(models.Model):
    hospital_name = models.CharField(max_length=30, unique=True)
    hospital_location = models.CharField(max_length=50)
    hospital_rank = models.IntegerField()
    hospital_message = models.TextField()
    beizhu1 = models.CharField(max_length=200,blank=True)
    beizhu2 = models.CharField(max_length=200,blank=True)
    beizhu3 = models.CharField(max_length=200,blank=True)

    def __str__(self):
        return self.hospital_name


# 科室表
class Department(models.Model):
    department_name = models.CharField(max_length=30, unique=True)
    department_message = models.TextField()
    beizhu1 = models.CharField(max_length=50,blank=True)
    beizhu2 = models.CharField(max_length=50,blank=True)
    beizhu3 = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.department_name

# 医院de科室表
class Hospital_Department(models.Model):
    hospital_name = models.CharField(max_length=30)
    department_name = models.CharField(max_length=30)
    hospital_rank = models.IntegerField(null=True)
    agree = models.BooleanField(default=True)
