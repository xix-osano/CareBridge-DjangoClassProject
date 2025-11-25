from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, default="unspecified")  # added default
    medical_record_number = models.CharField(max_length=50, unique=True)
    phone_number = models.CharField(max_length=10)
    medical_history = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class MedicalRecord(models.Model):
    patient_name = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=100)
    record_date = models.DateField(auto_now_add=True)
    diagnosis = models.TextField()
    treatment = models.TextField()

    def __str__(self):
        return f"Record for {self.patient_name} on {self.record_date}"
    

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    datetime = models.DateTimeField()
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return f"Appointment for {self.name} with Dr. {self.doctor} on {self.datetime}"
