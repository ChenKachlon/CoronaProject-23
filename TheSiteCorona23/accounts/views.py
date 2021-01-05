from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *

# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        context = {'form':form}
        return render(request,'accounts/register.html',context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Incorrect username OR password')
        context = {}
        return render(request, 'accounts/login.html', context)


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    pati=Patient.objects.all()
    bedi=Bed.objects.all()
    ven=Ventilator.objects.all()
    beds=bedi.count()
    xx=ven.count()
    free_beds=beds-pati.count()
    if(free_beds<0):
        free_beds='shortage of beds'
    context = {
             'beds': beds,
             'Ventilator': xx,
             'patients': pati,
             'freeBeds': free_beds
    }

    return render(request,'accounts/dashboard.html',context)

@login_required(login_url='login')
def patients(request):
    pat = Patient.objects.all()
    return render(request, 'accounts/patients.html', {'patients':pat})

@login_required(login_url='login')
def beds(request) :
    bedd = Bed.objects.all()
    return render(request,'accounts/beds.html',{'beds': bedd })

@login_required(login_url='login')
def ventilators(request) :
    venn = Ventilator.objects.all()
    return render(request,'accounts/Ventilators.html',{'Ventilators': venn})

@login_required(login_url='login')
def addPatients(request):
    form=PatientForm()
    if request.method=='POST':
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/patients_form.html',context)

@login_required(login_url='login')
def addBeds(request):
    form=BedForm()
    if request.method=='POST':
        form=BedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/beds_form.html',context)

@login_required(login_url='login')
def addVen(request):
    form=VenForm()
    if request.method=='POST':
        form=VenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/ventilators_form.html',context)

# def staff(request):
