from django.shortcuts import render,redirect

from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,RegisterForm,Add_seatsForm,Edit_appointForm
# Create your views here.
from doctor.models import Seats,Doctor
from client.models import Appointment,Patient
from django.http import HttpResponse
import time,hashlib


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


@check_session
def get_seats(request):
    userinfo = request.session.get('user_name')
    seats = Seats.objects.filter(name = userinfo)
    return render(request,'doc_seats.html',{'seats':seats})

@check_session
def del_seat(request,pk):
    if request.session.get('is_login',True):
        nid = pk
        Seats.objects.filter(id=nid).delete()
        return redirect('/doctor/')

    else:
        redirect('/blogs/')


@check_session
def add_seats(request):

    if request.method == "POST":

        newseatForm = Add_seatsForm(request.POST)
        message = "请检查填写的内容！"
        if  newseatForm.is_valid():  # 获取数据
            depart = newseatForm.cleaned_data['depart']
            brief = newseatForm.cleaned_data['brief']
            starttime = newseatForm.cleaned_data['starttime']
            endtime = newseatForm.cleaned_data['endtime']


            new_seat={}
            new_seat['name'] = request.session.get('user_name')
            new_seat['seat_num'] = create_id()
            new_seat['brief']= brief
            new_seat['starttime'] = starttime
            new_seat['endtime'] = endtime
            print(new_seat)
            new_seat = Seats.objects.create(**new_seat)
            new_seat.save()
            return redirect('/doctor')  # 自动跳转到登录页面
        else:
            print('阿斯顿发送到高')
            return redirect('/doctor')

    else:
        newseatForm = Add_seatsForm()
        return render(request,'add_seats.html',locals())



@check_session
def get_appoint(request):
    userinfo = request.session.get('user_name')
    appoint= Appointment.objects.filter(doctor_name = userinfo)
    return render(request,'appoint.html',{'appoint':appoint})


def edit_appoint(request,pk):
    if request.session.get('is_login',True):
        # 登录状态不允许注册。你可以修改这条原则！

        if request.method == "POST":

            newappoint_form = Edit_appointForm(request.POST)
            message = "请检查填写的内容！"
            if newappoint_form.is_valid():  # 获取数据
                docmessage = newappoint_form.cleaned_data['doc_message']
                D_agree = newappoint_form.cleaned_data['YN']

                appoint =  Appointment.objects.get(id=pk)
                appoint.doc_message = docmessage
                appoint.agree = D_agree
                appoint.save()

                return redirect('/D_appoint')  # 自动跳转到登录页面
            else:
                pass

        else:
            pk = pk
            newappoint_form = Edit_appointForm()
            return render(request,'edit_appoint.html',locals())
    return  redirect('/login/')

def doc_patient(request,nameinfo):
    patient = Patient.objects.filter(name = nameinfo)
    return render(request, 'client.html', {'patient': patient})


