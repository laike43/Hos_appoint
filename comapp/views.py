from django.shortcuts import render,redirect

from django.http import HttpResponseRedirect
from doctor.models import Doctor,Seats
from client.models import Patient,Appointment
from comapp.models import Blog
from comapp.forms import LoginForm,RegisterForm
# Create your views here.
#权限管理
def check_session(func):
    ''' check user session '''
    def wrapper(request,*args, **kv):
        userinfo=request.session.get('category')
        print(userinfo)
        if not userinfo:
            return HttpResponseRedirect('/login/') #没有登录，则跳转到登录页面
        return func(request,*args, **kv)
    return wrapper

def index(request):
    return render(request,'index.html')

def get_blog(request):
    blogs = Blog.objects.all().order_by('pub_date')
    #blogs = {'asd','asdasd','asd','asdasd'}
    return render(request,'blog_list.html',{'blogs':blogs})

def blog_deltail(request,pk):
    article = Blog.objects.get(pk=pk)

    return render(request,'blogs.html',{'article':article})


#登录
def login(request):
    if request.session.get('is_login',None):
        return redirect('blogs/1')

    if request.method == "POST":
        login_form = LoginForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            clientclass = login_form.cleaned_data['doc_client']
            try:
                if clientclass == 'doctor':
                    user = Doctor.objects.get(name=username)
                else:
                    user = Patient.objects.get(name=username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    request.session['category'] =  clientclass
                    if clientclass == 'doctor':
                        return redirect('/doctor')
                    else:
                        return redirect('/hospital')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login.html', locals())

    login_form = LoginForm()
    return render(request, 'login.html', locals())
# 注册
def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/blogs")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = models.User.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('/login/')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'register.html', locals())

def logout(request):
    if not request.session.get('is_login',None):
        return redirect('/login')
    request.session.flush()
    return redirect('/')





# sgg
def get_seats(request):
    seats = Seats.objects.all()
    return render(request,'app_seats.html',{'seats':seats})


def  center(request):
    userinfo = request.session.get('category')
    if userinfo == 'doctor':
        return redirect('/D_appoint')
    else:

        return redirect('/C_appoint')