from django.shortcuts import render,redirect

# Create your views here.
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from client.forms import LoginForm,AppointmentForm
# Create your views here.
from doctor.models import Seats,Doctor
from client.models import Patient,Appointment

import itertools
# 权限管理
def check_session(func):
    ''' check user session '''
    def wrapper(request,*args, **kv):
        userinfo=request.session.get('category')

        if  userinfo and userinfo=='client':
            return func(request, *args, **kv)
        else:
            return HttpResponseRedirect('/login/') #没有登录，则跳转到登录页面
    return wrapper


@check_session
def get_seats(request):
    seats = Seats.objects.all()
    return render(request,'C_seat.html',{'seats':seats})

@check_session
def get_appoint(request):
    userinfo = request.session.get('user_name')
    appoint = Appointment.objects.filter(client_name = userinfo)
    return render(request,'C_appoint.html',{'appoint':appoint})

@check_session
def add_apoint(request,seatnum,doctor_name):
    if request.method == "POST":

        newappoint_form = AppointmentForm(request.POST)
        message = "请检查填写的内容！"

        if newappoint_form.is_valid():  # 获取数据
            username = request.session.get('user_name')
            appointNum = seatnum
            message = newappoint_form.cleaned_data['message']

            new_appoint={}
            new_appoint['client_name'] = username
            new_appoint['doctor_name'] = doctor_name

            new_appoint['seat_num'] = appointNum
            new_appoint['client_message']= message
            new_appoint['doc_message'] = '待回复'
            new_appoint['agree'] = None
            print(new_appoint)
            new_appoint = Appointment.objects.create(**new_appoint)
            new_appoint.save()
            print('suessefr                   sdfsdfsdf             sddffsdf            sdfsd ')
            return redirect('/client')

        else:
            return render(request,'add_appoint.html',locals())

    else:
        seatnum = seatnum
        newappoint_form = AppointmentForm()
        return render(request,'add_appoint.html',locals())
@check_session
def del_apoint(request,pk):

    nid = pk
    Appointment.objects.filter(id=nid).delete()
    return redirect('/client')


@check_session
def appointdetail(request,seat_num):
    app ={}
    appoint = Appointment.objects.filter(seat_num = seat_num)
    for i in appoint:
        app['client'] = i.client_name
        app['C_message'] = i.client_message
        app['D_message'] = i.doc_message
        app['agree'] = i.agree
    seats = Seats.objects.filter(seat_num = seat_num)
    for i in seats:
        app['seat_num']=i.seat_num
        app['name'] = i.name
        app['starttime']=i.starttime
        app['endtime'] = i.endtime
    return render(request, 'C_app_detail.html',app)

def get_hospital(request,hopital_name):
    hospital = Doctor.object.filter(infirmary = hopital_name)


    return render(request,'')

