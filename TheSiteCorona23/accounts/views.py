from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
from .decorators import *

# Create your views here.


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


@unauthenticated_user
def loginPage(request):
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
@manger_only
def home(request):
    pati=Patient.objects.all()
    bedi=Bed.objects.all()
    ven=Ventilator.objects.all()
    beds=bedi.count()
    xx=ven.count()
    free_beds=beds-pati.count()
    if(free_beds<0):
        free_beds='Shortage of beds!!!'
    context = {
             'beds': beds,
             'Ventilator': xx,
             'patients': pati,
             'freeBeds': free_beds
    }
    return render(request,'accounts/dashboard.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['senior', 'staff', 'help_desk'])
def departmentPage(request):
    context = {}
    return render(request, 'accounts/department.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['manger', 'help_desk'])
def patients(request):
    pat = Patient.objects.all()
    return render(request, 'accounts/patients.html', {'patients':pat})


@login_required(login_url='login')
@allowed_users(allowed_roles=['manger', 'help_desk'])
def bedsInDep(request):
    temp=Bed.objects.get('Corona')
    CoronaBed=temp.count
    temp1 = Bed.objects.get('Emergency Room')
    Emergency_Room_Bed = temp1.count
    temp2 = Bed.objects.get('Heart')
    HeartBed = temp2.count
    temp3 = Bed.objects.get('ENP')
    ENTbed = temp3.count
    context = {
             'Corona': CoronaBed,
             'Emergency Room': Emergency_Room_Bed,
             'Heart': HeartBed,
             'ENP': ENTbed
    }
    return render(request, 'accounts/beds.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['manger', 'help_desk'])
def beds(request) :
    bedd = Bed.objects.all()
    return render(request,'accounts/beds.html',{'beds': bedd })


@login_required(login_url='login')
@allowed_users(allowed_roles=['manger', 'help_desk'])
def ventilators(request) :
    venn = Ventilator.objects.all()
    return render(request,'accounts/Ventilators.html',{'Ventilators': venn})


@login_required(login_url='login')
@allowed_users(allowed_roles=['manger', 'help_desk'])
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
@allowed_users(allowed_roles=['manger', 'help_desk'])
def updatePatient(request,pk):
    patient = Patient.objects.get(id=pk)
    form = PatientForm(instance=patient)
    if request.method=='POST':
        form=PatientForm(request.POST,instance=patient)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/patients_form.html',context)

@login_required(login_url='login')
def deletePatient(request,pk):
    patient = Patient.objects.get(id=pk)
    if request.method=='POST':
        patient.delete()
        return redirect('/')
    context = {'patient':patient}
    return render(request,'accounts/delete_patient.html',context)



@login_required(login_url='login')
@allowed_users(allowed_roles=['manger', 'help_desk'])
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
@allowed_users(allowed_roles=['manger', 'help_desk'])
def addVen(request):
    form=VenForm()
    if request.method=='POST':
        form=VenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'accounts/ventilators_form.html',context)



# @login_required(login_url='login')
# def MaxConcentration(request):
#     # print('update the max concentration')
#     x = input()
#     # form=VenForm()
#     # if request.method=='POST':
#     # #     form=VenForm(request.POST)
#     # #     if form.is_valid():
#     #          form.save()
#     #         return redirect('/')
#     # context={'form':form}
#     return x
# def staff(request):
