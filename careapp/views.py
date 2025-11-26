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
        Appointment.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            datetime=request.POST.get("datetime"),
            department=request.POST.get("department"),
            doctor=request.POST.get("doctor"),
            message=request.POST.get("message","")
        )
        messages.success(request, "Your appointment has been scheduled.")
        return redirect("appointment")  # ensure url name matches
    return render(request, "appointment.html")

def departments(request):
    return render(request, 'departments.html')

def doctors(request):
    return render(request, 'doctors.html')

def show(request):
    appointments = Appointment.objects.all()
    return render(request, 'show.html', {"appointments": appointments})