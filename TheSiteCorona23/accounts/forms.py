from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'


class BedForm(ModelForm):
    class Meta:
        model = Bed
        fields = '__all__'


class VenForm(ModelForm):
    class Meta:
        model = Ventilator
        fields = '__all__'


class ConcentrationForm(ModelForm):
    class Meta:
        model = Concentration
        fields = '__all__'


class EquipForm(ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'


class ReqForm(ModelForm):
    class Meta:
        model = RequestForm
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    # Corona = forms.BooleanField(label='Corona')
    # ENP = forms.BooleanField(label='ENP')
    # Heart = forms.BooleanField(label='Heart')
    # Emergency_room = forms.BooleanField(label='Emergency room')
    #
    # if not Corona and not ENP and not Heart and not Emergency_room:
    #     raise forms.ValidationError("Must choose department")
    #
    # dep_select = forms.ChoiceField(
    #     widget=forms.RadioSelect,
    #     label="Choose department",
    #     choices=(('Corona', 'Corona'), ('ENP', 'ENP'), ('Heart', 'Heart'), ('Emergency_room', 'Emergency_room'))
    # )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]
