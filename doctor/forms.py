from django import forms

import datetime

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
class RegisterForm(forms.Form):
    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label='性别', choices=gender)
class Add_seatsForm(forms.Form):
    depart = forms.CharField(label="科室",max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    brief = forms.CharField(label="注意",max_length=500, widget=forms.Textarea(attrs={'class': 'form-control'}))
    starttime = forms.DateTimeField(label="开始时间 如:2016-06-03 13:00:00", widget=forms.DateTimeInput(attrs={'class': 'form-control'}))
    endtime = forms.DateTimeField(label="结束时间 如:2016-06-03 13:00:00",widget=forms.DateTimeInput( attrs = {'class': 'form-control'}))

class Edit_appointForm(forms.Form):
    gender = (
        ('False', "拒绝"),
        ('True', "通过"),
    )
    doc_message = forms.CharField(label="回复信息", max_length=128, widget=forms.Textarea(attrs={'class': 'form-control'}))
    YN = forms.ChoiceField(label='是否通过', choices=gender)