from django import forms
from .models import *
class LoginForm(forms.Form):
    username = forms.CharField(label = 'Tài khoản', max_length= 50)
    password =  forms.CharField(label= 'Mật khẩu',widget= forms.PasswordInput())
class TeacherRegisterForm(forms.Form):
    fullname = forms.CharField(label = 'Họ Tên', max_length= 30)
    khoa = forms.CharField(label='Khoa/Viện',max_length=30)
    email = forms.CharField(label='Email/SĐT',max_length=30)
    password =  forms.CharField(label= 'Mật khẩu',widget= forms.PasswordInput())
    def save(self):
        fullname = self.cleaned_data['fullname']
        password = self.cleaned_data['password']
        khoa = self.cleaned_data['khoa']
        email = self.cleaned_data['email']
        a =lecturer(name = fullname,phone_mail= email,institute= khoa)
        b = acount(username = email,password= password)
        b.save()
        a.save()
class CreatClass(forms.Form):
    subname = forms.CharField(label='Tên Môn Học:', max_length=30)
    subcode = forms.CharField(label='Mã Học Phần:',max_length=30)
    classname = forms.CharField(label='Mã Lớp Học:',max_length=30)
class AddMem(forms.Form):
    mssv = forms.CharField(label='Nhập mã số sinh viên:',max_length=30)
class UpdatePoint(forms.Form):
    gk= forms.FloatField(label='Diem Giua Ki:')
    ck = forms.FloatField(label='Diem Cuoi Ki:')