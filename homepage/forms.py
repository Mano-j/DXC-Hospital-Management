from django import forms
from .models import PatientDetails, DoctorDetails

class postForm(forms.ModelForm):
    
    CRITICALITY_CHOICES = [
        ('N', "Normal",),
        ('U', "Urgent",),
        ('E', "Emergency",),
    ]

    criticality = forms.ChoiceField(
        label="How critical is the situation?", 
        widget=forms.RadioSelect(),
        choices=CRITICALITY_CHOICES
    )

    class Meta:
        model = PatientDetails
        fields = ["patient_name", "patient_age", "patient_DOB", "patient_sex", "marital_status", "patient_height", "patient_weight", "reason_for_consultation", "criticality", "insurance"]

