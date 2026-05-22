from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import (
    Booking,
    CustomUser,
    MedicalReport
)


# ---------------------------
# DOCTOR REGISTER FORM
# ---------------------------

class DoctorRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser

        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


# ---------------------------
# PATIENT REGISTER FORM
# ---------------------------

class PatientRegisterForm(UserCreationForm):

    class Meta:
        model = CustomUser

        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]


# ---------------------------
# BOOKING FORM
# ---------------------------

class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = [
            'patient_name',
            'patient_email',
            'patient_phone',
            'doctor',
            'appointment_date',
            'appointment_time'
        ]

        widgets = {

            'appointment_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'appointment_time': forms.TimeInput(
                attrs={
                    'type': 'time',
                    'class': 'form-control'
                }
            ),

        }


# ---------------------------
# MEDICAL REPORT FORM
# ---------------------------

class MedicalReportForm(forms.ModelForm):

    class Meta:
        model = MedicalReport

        fields = [
            'patient',
            'report_name',
            'report_file'
        ]