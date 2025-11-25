from django.shortcuts import render, redirect
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
            name=request.POST.get('name'),
            email=request.POST.get('email'),
            phone=request.POST.get('phone'),
            datetime=request.POST.get('date'),
            department=request.POST.get('department'),
            doctor=request.POST.get('doctor'),
            message=request.POST.get('message'),
        ).save()
        return redirect('/appointment')
    return render(request, 'appointment.html')

def departments(request):
    return render(request, 'departments.html')

def doctors(request):
    return render(request, 'doctors.html')