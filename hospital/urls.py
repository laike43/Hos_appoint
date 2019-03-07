"""hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from doctor import views as dov
from client import views as clv
from comapp import views as cmv
from infirmary import views as inv

urlpatterns = [
    path('admin/', admin.site.urls),

    path('',cmv.index),
    path('blogs/',cmv.get_blog),
    path('blogs/<int:pk>/', cmv.blog_deltail),
    path('login/',cmv.login),
    path('register/',cmv.register),
    path('logout/',cmv.logout),
    path('index/',cmv.index),
    path('center/',cmv.center),




    path('doctor/',dov.get_seats),
    path('D_appoint/',dov.get_appoint),
    path('doc_pat/<str:nameinfo>',dov.doc_patient),

    path('add_seats/',dov.add_seats),
    path('del_seats/<int:pk>',dov.del_seat),
    path('edit/<int:pk>',dov.edit_appoint),






    path('client',clv.get_seats),
    path('C_appoint',clv.get_appoint),
    path('appoint-detail/<str:seat_num>',clv.appointdetail),

    path('add_appoint/<str:seatnum>/<str:doctor_name>',clv.add_apoint),
    path('del_appoint/<int:pk>',clv.del_apoint),


    path('hospital/',inv.get_hospital),
    path('department/<str:hospital_name>',inv.get_depart),
    path('doctorlist/<str:hospital>/<str:depart>',inv.get_doctor),
    path('seats/<str:doctor_name>',inv.get_seat),

]
