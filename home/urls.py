from django.urls import path
from . import views

urlpatterns = [

    # Login
    path('', views.user_login, name='login'),

    # Home Pages
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

    # Doctors + Departments
    path('doctors/', views.doctors_view, name='doctors'),
    path('departments/', views.departments, name='departments'),

    # Booking
    path('booking/', views.booking, name='booking'),

    # Authentication
    path('doctor_register/', views.doctor_register, name='doctor_register'),
    path('patient_register/', views.patient_register, name='patient_register'),

    path('logout/', views.user_logout, name='logout'),

    # Dashboard
    path('doctor_dashboard/', views.doctor_dashboard, name='doctor_dashboard'),

    # Medical Reports
    path('upload_report/', views.upload_report, name='upload_report'),
    path('view_reports/', views.view_reports, name='view_reports'),
]