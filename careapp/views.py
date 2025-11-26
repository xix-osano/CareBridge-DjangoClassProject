from django.shortcuts import render, redirect
from django.contrib import messages
from careapp.models import *

# Create your views here.

def home(request):
    return render(request, 'index.html')

def starter(request):
    return render(request, 'starter-page.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def Appoint(request):
    if request.method == "POST":
        Appointment(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            datetime=request.POST['date'],
            department=request.POST['department'],
            doctor=request.POST['doctor'],
            message=request.POST['message'],
        ).save()
        messages.success(request, 'Your appointment has been booked successfully!!')
        return redirect('/appointment')
    return render(request, 'appointment.html')

def departments(request):
    return render(request, 'departments.html')

def doctors(request):
    return render(request, 'doctors.html')

def show(request):
    appointments = Appointment.objects.all()
    return render(request, 'show.html', {"appointments": appointments})