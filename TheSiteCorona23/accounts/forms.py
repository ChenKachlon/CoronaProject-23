from django.forms import ModelForm
from .models import *

class PatientForm(ModelForm):
    class Meta:
        model=Patient
        fields ='__all__'

class BedForm(ModelForm):
    class Meta:
        model=Bed
        fields ='__all__'

class VenForm(ModelForm):
    class Meta:
        model=Ventilator
        fields ='__all__'