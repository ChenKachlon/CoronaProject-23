from django.contrib import admin
from .models import *

# Register our models here.
admin.site.register(Patient)
admin.site.register(Bed)
admin.site.register(Ventilator)
admin.site.register(Concentration)
admin.site.register(Equipment)
admin.site.register(RequestForm)
admin.site.register(ReportForm)
admin.site.register(Department)

