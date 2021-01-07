from django.contrib import admin
from .models import Patient
from .models import Bed
from .models import Ventilator
from .models import Concentration
from .models import Equipment
from .models import RequestForm

# Register your models here.
admin.site.register(Patient)
admin.site.register(Bed)
admin.site.register(Ventilator)
admin.site.register(Concentration)
admin.site.register(Equipment)
admin.site.register(RequestForm)