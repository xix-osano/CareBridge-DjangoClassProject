from django.shortcuts import render, redirect, get_object_or_404
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
            name=request.POST["name"],
            email=request.POST["email"],
            phone=request.POST["phone"],
            datetime=request.POST["datetime"],
            department=request.POST["department"],
            doctor=request.POST["doctor"],
            message=request.POST["message"]
        ).save()
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

def delete(request, id):
    # appointment = get_object_or_404(Appointment, id=id)
    appointment = Appointment.objects.get(id=id)
    appointment.delete()
    messages.success(request, "Appointment deleted successfully.")
    return redirect("show")  # ensure url name matches

def edit(request, id):
    appointment = get_object_or_404(Appointment, id=id)
    if request.method == "POST":
        appointment.name = request.POST.get("name")
        appointment.email = request.POST.get("email")
        appointment.phone = request.POST.get("phone")
        appointment.datetime = request.POST.get("datetime")
        appointment.department = request.POST.get("department")
        appointment.doctor = request.POST.get("doctor")
        appointment.message = request.POST.get("message","")
        appointment.save()
        messages.success(request, "Appointment updated successfully.")
        return redirect("show")  # ensure url name matches
    return render(request, "edit.html", {"appointment": appointment})