from django.db import models

# Create your models here.
class doctor(models.Model):
    doctor_name=models.CharField(max_length=100)
    doctor_fees=models.IntegerField()
    doctor_email=models.EmailField()
    doctor_number=models.BigIntegerField()
    doctor_image=models.ImageField()
    doctor_dept=models.CharField(max_length=200)
    doctor_avail_date=models.DateTimeField()



    def __str__ (self):
        return self.doctor_name
    

class Appointment(models.Model):
    patient_name = models.CharField(max_length=100)
    patient_phone = models.BigIntegerField()

    doctor = models.ForeignKey(doctor, on_delete=models.CASCADE)

    appointment_date = models.DateField()
    appointment_time = models.TimeField()

    status = models.CharField(max_length=20, default="Pending")

    def __str__(self):
        return self.patient_name


