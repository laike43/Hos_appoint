from django.shortcuts import render,redirect

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from doctor.models import Seats,Doctor
from client.models import Appointment,Patient
from django.http import HttpResponse
import time,hashlib
from infirmary.models import Hospital_Department,Hospital,Department

# Create your views here.



# 唯一数 num 生成
def create_id():
    m = hashlib.md5(str(time.time()).encode('utf-8'))
    return m.hexdigest()

# 权限管理
def check_session(func):
    ''' check user session '''
    def wrapper(request,*args, **kv):
        userinfo=request.session.get('category')

        if  userinfo and userinfo=='doctor':
            return func(request, *args, **kv)
        else:
            return HttpResponseRedirect('/login/') #没有登录，则跳转到登录页面
    return wrapper



def get_hospital(request):
    hospital = Hospital.objects.all()
    return render(request,'hospital.html',{'hospital':hospital})

def get_depart(request,hospital_name):

    depart = Hospital_Department.objects.filter(hospital_name=hospital_name)
    return render(request, 'depart.html', {'depart': depart})

def get_doctor(request,hospital,depart):
    print(hospital,depart)
    doctor = Doctor.objects.filter(infirmary = hospital,department= depart)

    return render(request, 'doctor.html', {'doctor': doctor})

def get_seat(request,doctor_name):

    seats = Seats.objects.filter(name=doctor_name)

    return render(request, 'C_seat.html', {'seats': seats})








