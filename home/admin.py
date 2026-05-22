from django.contrib import admin

# Register your models here.
from . models import (
    Department,
    Doctors,
    Booking,
    CustomUser,
    MedicalReport
)

admin.site.register(Department)
admin.site.register(Doctors)
admin.site.register(Booking)
admin.site.register(CustomUser)
admin.site.register(MedicalReport)