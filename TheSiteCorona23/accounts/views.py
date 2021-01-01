from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
def home(request):
    pati=Patient.objects.all()
    bedi=Bed.objects.all()
    ven=Ventilator.objects.all()
    patients=pati.count()
    beds=bedi.count()
    xx=ven.count()
    context = {'patients':patients,
             'beds':beds,
             'Venentilators':xx,
            'patients':pati}

    return render(request,'accounts/dashboard.html',context)

def patients(request):
    pat=Patient.objects.all()
    return render(request,'accounts/patients.html',{'patients':pat})

def beds(request) :
    bedd = Bed.objects.all()
    return render(request,'accounts/beds.html',{'beds': bedd})

def ventilators(request) :
    venn = Ventilator.objects.all()
    return render(request,'accounts/Ventilators.html',{'Ventilators': venn})
