from django.contrib import admin
from .models import Patient
from .models import Bed
from .models import Ventilator

# Register your models here.
admin.site.register(Patient)
admin.site.register(Bed)
admin.site.register(Ventilator)
