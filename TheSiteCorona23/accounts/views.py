from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *
def home(request):
    pati=Patient.objects.all()
    bedi=Bed.objects.all()
    ven=Ventilator.objects.all()
    beds=bedi.count()
    xx=ven.count()
    free_beds=beds-pati.count()
    context = {
             'beds':beds,
             'Ventilator':xx,
             'patients':pati,
             'freeBeds':free_beds
    }

    return render(request,'accounts/dashboard.html',context)

def patients(request):
    pat=Patient.objects.all()
    return render(request,'accounts/patients.html',{'patients':pat})

def beds(request) :
    bedd = Bed.objects.all()
    # addbedd = bedd.addBeds()
    return render(request,'accounts/beds.html',{'beds': bedd })
    # , 'addBed': addbedd

def ventilators(request) :
    venn = Ventilator.objects.all()
    return render(request,'accounts/Ventilators.html',{'Ventilators': venn})
