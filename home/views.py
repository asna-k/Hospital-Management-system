from django.shortcuts import render, redirect
from django.core.mail import send_mail

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Department, Doctors, Booking, MedicalReport
from .forms import (
    BookingForm,
    DoctorRegisterForm,
    PatientRegisterForm,
    MedicalReportForm
)

# ===========================
# HOME / BASIC PAGES
# ===========================

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def about(request):
    return render(request, 'about.html')


@login_required(login_url='login')
def contact(request):
    return render(request, 'contact.html')


# ===========================
# DEPARTMENTS
# ===========================

@login_required(login_url='login')
def departments(request):

    dept = Department.objects.all()

    return render(request, 'departments.html', {
        'dept': dept
    })


# ===========================
# DOCTORS LIST
# ===========================

@login_required(login_url='login')
def doctors_view(request):

    doctors = Doctors.objects.all()

    return render(request, 'doctors.html', {
        'doctors': doctors
    })


# ===========================
# BOOKING APPOINTMENT
# ===========================

@login_required(login_url='login')
def booking(request):

    if request.method == 'POST':

        form = BookingForm(request.POST)

        if form.is_valid():

            booking_obj = form.save()

            # Send Email
            send_mail(
                subject='Appointment Confirmation',

                message=f'''
Hello {booking_obj.patient_name},

Your appointment has been booked successfully.

Doctor : {booking_obj.doctor.doc_name}
Date   : {booking_obj.appointment_date}
Time   : {booking_obj.appointment_time}

Thank You,
CityCare Hospital
                ''',

                from_email='your_email@gmail.com',

                recipient_list=[booking_obj.patient_email],

                fail_silently=False
            )

            return render(request, 'confirmation.html')

    else:

        form = BookingForm()

    return render(request, 'booking.html', {
        'form': form
    })


# ===========================
# DOCTOR REGISTER
# ===========================

def doctor_register(request):

    if request.user.is_authenticated:
        return redirect('home')

    form = DoctorRegisterForm()

    if request.method == 'POST':

        form = DoctorRegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # role field model-il undenkil
            user.role = 'doctor'

            user.save()

            return redirect('login')

    return render(request, 'doctor_register.html', {
        'form': form
    })


# ===========================
# PATIENT REGISTER
# ===========================

def patient_register(request):

    if request.user.is_authenticated:
        return redirect('home')

    form = PatientRegisterForm()

    if request.method == 'POST':

        form = PatientRegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # role field model-il undenkil
            user.role = 'patient'

            user.save()

            return redirect('login')

    return render(request, 'patient_register.html', {
        'form': form
    })


# ===========================
# LOGIN
# ===========================

def user_login(request):

    # already logged in
    if request.user.is_authenticated:

        role = getattr(request.user, 'role', None)

        if role == 'doctor':
            return redirect('doctor_dashboard')

        return redirect('home')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            role = getattr(user, 'role', None)

            if role == 'doctor':
                return redirect('doctor_dashboard')

            return redirect('home')

        else:

            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login.html')


# ===========================
# LOGOUT
# ===========================

def user_logout(request):

    logout(request)

    return redirect('login')


# ===========================
# DOCTOR DASHBOARD
# ===========================

@login_required(login_url='login')
def doctor_dashboard(request):

    if getattr(request.user, 'role', None) != 'doctor':
        return redirect('home')

    return render(request, 'doctor_dashboard.html')


# ===========================
# UPLOAD REPORT
# ===========================

@login_required(login_url='login')
def upload_report(request):

    if getattr(request.user, 'role', None) != 'doctor':
        return redirect('home')

    if request.method == 'POST':

        form = MedicalReportForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            return redirect('doctor_dashboard')

    else:

        form = MedicalReportForm()

    return render(request, 'upload_report.html', {
        'form': form
    })


# ===========================
# VIEW REPORTS
# ===========================

@login_required(login_url='login')
def view_reports(request):

    if getattr(request.user, 'role', None) != 'doctor':
        return redirect('home')

    reports = MedicalReport.objects.all()

    return render(request, 'view_reports.html', {
        'reports': reports
    })