from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request, 'accounts/dashboard.html')

def login(request):
	return render(request, 'accounts/login.html')

def patient(request):
	return render(request, 'accounts/patient.html')