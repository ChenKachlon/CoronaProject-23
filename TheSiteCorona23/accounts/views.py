from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import *
def home(request):
    pati=Patient.objects.all()
    bedi=Bed.objects.all()
    ven=Ventilator.objects.all()
    beds=bedi.count()
    xx=ven.count()
    free_beds=beds-pati.count()
    context = {
             'beds': beds,
             'Ventilator': xx,
             'patients': pati,
             'freeBeds': free_beds
    }

    return render(request,'accounts/dashboard.html',context)

def patients(request):
    pat=Patient.objects.all()
    return render(request,'accounts/patients.html',{'patients':pat})

def beds(request) :
    bedd = Bed.objects.all()
    return render(request,'accounts/beds.html',{'beds': bedd })

def ventilators(request) :
    venn = Ventilator.objects.all()
    return render(request,'accounts/Ventilators.html',{'Ventilators': venn})

def addPatients(request):
    form=PatientForm()
    if request.method=='POST':
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/patients_form.html',context)

def addBeds(request):
    form=BedForm()
    if request.method=='POST':
        form=BedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/beds_form.html',context)

def addVen(request):
    form=VenForm()
    if request.method=='POST':
        form=VenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/ventilators_form.html',context)
