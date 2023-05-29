from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from StudentApp.models import City, Course, Student


# Create your views here.
def reg_fun(request):
    return render(request, 'register.html',{'data':''})


def regdata_fun(request):
    user_name = request.POST['txtUserName']
    user_email = request.POST['txtUserEmail']
    user_pswd = request.POST['txtUserPswd']
    if User.objects.filter(Q(username=user_name) | Q(email=user_email)).exists():
        return render(request, 'register.html',{'data':'username and Email is already exists'})
    else:
        u1= User.objects.create_superuser(username=user_name,email=user_email,password=user_pswd)
        u1.save()
        return redirect('log')


def log_fun(request):
    return render(request,'login.html',{'data':''})


def logdata_fun(request):
    user_name = request.POST['txtUserName']
    user_pswd = request.POST['txtUserPswd']
    user1 = authenticate(username=user_name,password=user_pswd)
    if user1 is not None:
        if user1.is_superuser:
            return redirect('home')
        else:
            return render(request,'login.html',{'data':'user is not a superuser'})
    else:
        return render(request, 'login.html',{'data':'enter proper username and password'})


def home_fun(request):
    return render(request,'home.html')


def addstudent_fun(request):
    city = City.objects.all()
    course = Course.objects.all()
    return render(request,'addstudent.html',{'City_Data':city,'Course_Data':course})


def readdata_fun(request):
    s1 = Student()
    s1.Student_Name = request.POST['txtName']
    s1.Student_Age = request.POST['txtAge']
    s1.Student_Phno = request.POST['txtPhno']
    s1.Student_City = City.objects.get(City_Name =request.POST['ddlCity'])
    s1.Student_Course = Course.objects.get(Course_Name = request.POST['ddlCourse'])
    s1.save()
    return redirect('add')