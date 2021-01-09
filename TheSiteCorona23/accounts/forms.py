from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class PatientForm(ModelForm):
    """class that make a form of Patient"""
    class Meta:
        model = Patient
        fields = '__all__'


class BedForm(ModelForm):
    """class that make a form of Bed"""
    class Meta:
        model = Bed
        fields = '__all__'


class VenForm(ModelForm):
    """class that make a form of Ventilator"""
    class Meta:
        model = Ventilator
        fields = '__all__'


class ConcentrationForm(ModelForm):
    """class that make a form of Concentration"""
    class Meta:
        model = Concentration
        fields = '__all__'


class EquipForm(ModelForm):
    """class that make a form of Equipment"""
    class Meta:
        model = Equipment
        fields = '__all__'


class ReqForm(ModelForm):
    """class that make a form of Request"""
    class Meta:
        model = RequestForm
        fields = '__all__'


class RepForm(ModelForm):
    """class that make a form of Report"""
    class Meta:
        model = ReportForm
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    """class that make a form of Creation user"""
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', ]


class EmployeeForm(ModelForm):
    """class that make a form of Employee"""
    class Meta:
        model = Department
        fields = ['department', ]
