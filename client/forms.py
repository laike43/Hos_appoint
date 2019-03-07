from django import forms

import datetime

class LoginForm(forms.Form):
    gender = (
        ('doctor', "医生"),
        ('client', "用户"),
    )
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    doc_client = forms.ChoiceField(label='用户类别', choices=gender)

class AppointmentForm(forms.Form):
    message = forms.CharField(label="病情", max_length=128, widget=forms.Textarea(attrs={'class': 'form-control'}))

