from django.db import models
from django.core.validators import MaxValueValidator
from django import forms
from django.utils import timezone



class DoctorDetails(models.Model):
    doctor_name = models.CharField(max_length=50)
    doctor_availability = models.BooleanField(default=True)
    doctor_specialisation = models.CharField(max_length=200)
    doctor_sex = models.CharField(
        max_length=1,
        default='F',
        choices=(
        ('F', 'Female',),
        ('M', 'Male',),
        ('T', 'Transgender',),
    )
    )
    is_Doctor_servicing = models.BooleanField(default=True)
    remaining_time = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.doctor_name


class PatientDetails(models.Model):
    patient_name = models.CharField(max_length=100, null=True)
    patient_age = models.IntegerField(validators=[MaxValueValidator(150)], null=True)
    patient_DOB = models.DateField(null=True)
    marital_status = models.CharField(max_length=100, null=True)
    patient_new = models.BooleanField(default=True)
    insurance = models.CharField(max_length=100, null=True)
    patient_height = models.IntegerField(null=True)
    patient_weight = models.IntegerField(null=True)
    patient_sex = models.CharField(
        max_length=1,
        default='F',
        choices=(
        ('F', 'Female',),
        ('M', 'Male',),
        ('T', 'Transgender',),
    )
    )
    criticality = models.CharField(max_length=20)
    reason_for_consultation = models.CharField(max_length=300, null=True)    
    
    appointment_form_submission_date_time = models.DateTimeField(auto_now_add=True, null=True)    

    doctorDetails = models.ForeignKey(DoctorDetails, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return self.patient_name
    

