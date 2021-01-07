from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Patient)
admin.site.register(Bed)
admin.site.register(Ventilator)
admin.site.register(Concentration)
admin.site.register(Equipment)
admin.site.register(RequestForm)
admin.site.register(Department)
