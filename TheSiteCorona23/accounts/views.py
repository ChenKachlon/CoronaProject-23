from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
from .decorators import *


# Create your views here.


@unauthenticated_user
def registerPage(request):
    if request.method == 'POST':
        user_form = CreateUserForm(request.POST)
        employee_form = EmployeeForm(request.POST)
        if user_form.is_valid() and employee_form.is_valid():
            user = user_form.save()
            employee = employee_form.save(commit=False)
            group = Group.objects.get(name='staff')
            user.groups.add(group)
            username = user_form.cleaned_data.get('username')
            employee.user = user
            employee.save()
            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
    else:
        user_form = UserCreationForm()
        employee_form = EmployeeForm()
    context = {'user_form': user_form, 'employee_form': employee_form}
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
    pati = Patient.objects.all()
    bedi = Bed.objects.all()
    ven = Ventilator.objects.all()
    beds = bedi.count()
    xx = ven.count()
    free_beds = 0
    for i in Bed.objects.all():
        if i.name == 'Unknown':
            free_beds += 1
    concentration = Concentration.objects.all()[0]
    if free_beds < 0:
        free_beds = 'Shortage of beds!!!'
    context = {
        'concentration': concentration,
        'beds': beds,
        'Ventilator': xx,
        'patients': pati,
        'freeBeds': free_beds
    }
    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['senior', 'staff', 'help_desk'])
def departmentPage(request, pk_dep):
    dep = Department.objects.get(id=pk_dep)
    dep_name = dep.department
    patient = Patient.objects.all()
    all_beds = Bed.objects.all()
    all_ven = Ventilator.objects.all()
    dep_beds = 0
    dep_ven = 0
    free_beds = 0
    for i in all_beds:
        if i.department == dep_name:
            dep_beds += 1
            if i.name == 'Unknown':
                free_beds += 1
    for i in all_ven:
        if i.department == dep_name:
            dep_ven += 1
    context = {'department': dep_name, 'beds': dep_beds,
               'Ventilator': dep_ven, 'patients': patient,
               'freeBeds': free_beds}
    return render(request, 'accounts/department.html', context)


@login_required(login_url='login')
@manger_only
def patients(request):
    temp = Patient.objects.all()
    mildly = temp.filter(status='mildly ill').count()
    medium = temp.filter(status='medium ill').count()
    seriously = temp.filter(status='seriously ill').count()
    dying = temp.filter(status='dying').count()
    need_ven = temp.filter(need_ven='YES').count()
    context = {
        'need_ven': need_ven,
        'patients': temp,
        'mildly': mildly,
        'medium': medium,
        'seriously': seriously,
        'dying': dying,
    }
    return render(request, 'accounts/patients.html', context)


@login_required(login_url='login')
@manger_only
def beds(request):
    temp = Bed.objects.all()
    Corona = temp.filter(department='Corona').count()
    EmergencyRoom = temp.filter(department='Emergency room').count()
    Heart = temp.filter(department='Heart').count()
    ENP = temp.filter(department='ENP').count()
    context = {
        'beds': temp,
        'Corona': Corona,
        'EmergencyRoom': EmergencyRoom,
        'Heart': Heart,
        'ENP': ENP,
    }
    return render(request, 'accounts/beds.html', context)


@login_required(login_url='login')
@manger_only
def ventilators(request):
    temp = Ventilator.objects.all()
    Corona = temp.filter(department='Corona').count()
    EmergencyRoom = temp.filter(department='Emergency room').count()
    Heart = temp.filter(department='Heart').count()
    ENP = temp.filter(department='ENP').count()
    context = {
        'Ventilators': temp,
        'Corona': Corona,
        'EmergencyRoom': EmergencyRoom,
        'Heart': Heart,
        'ENP': ENP,
    }
    return render(request, 'accounts/ventilators.html', context)


@login_required(login_url='login')
def addPatients(request):
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        form.department = 'Corona'
        if form.is_valid():
            form.save()
            return redirect('/patients/')
    context = {'form': form}
    return render(request, 'accounts/patients_form.html', context)


@login_required(login_url='login')
@manger_only
def updatePatient(request, pk):
    patient = Patient.objects.get(id=pk)
    form = PatientForm(instance=patient)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('/patients/')
    context = {'form': form}
    return render(request, 'accounts/patients_form.html', context)


@login_required(login_url='login')
@manger_only
def deletePatient(request, pk):
    patient = Patient.objects.get(id=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('/patients/')
    context = {'patient': patient}
    return render(request, 'accounts/delete_patient.html', context)


@login_required(login_url='login')
@manger_only
def addBeds(request):
    form = BedForm()
    if request.method == 'POST':
        form = BedForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/beds/')
    context = {'form': form}
    return render(request, 'accounts/beds_form.html', context)


@login_required(login_url='login')
@manger_only
def updateBeds(request, pk):
    bed = Bed.objects.get(id=pk)
    form = BedForm(instance=bed)
    if request.method == 'POST':
        form = BedForm(request.POST, instance=bed)
        if form.is_valid():
            form.save()
            return redirect('/beds/')
    context = {'form': form}
    return render(request, 'accounts/beds_form.html', context)


@login_required(login_url='login')
@manger_only
def deleteBed(request, pk):
    bed = Bed.objects.get(id=pk)
    if request.method == 'POST':
        bed.delete()
        return redirect('/beds/')
    context = {'bed': bed}
    return render(request, 'accounts/beds_form.html', context)


@login_required(login_url='login')
@manger_only
def addVen(request):
    form = VenForm()
    if request.method == 'POST':
        form = VenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ventilators/')
    context = {'form': form}
    return render(request, 'accounts/ventilators_form.html', context)


@login_required(login_url='login')
@manger_only
def updateVen(request, pk):
    ven = Ventilator.objects.get(id=pk)
    form = VenForm(instance=ven)
    if request.method == 'POST':
        form = VenForm(request.POST, instance=ven)
        if form.is_valid():
            form.save()
            return redirect('/ventilators/')
    context = {'form': form}
    return render(request, 'accounts/ventilators_form.html', context)


@login_required(login_url='login')
@manger_only
def deleteVen(request, pk):
    ven = Ventilator.objects.get(id=pk)
    if request.method == 'POST':
        ven.delete()
        return redirect('/ventilators/')
    context = {'ven': ven}
    return render(request, 'accounts/ventilators_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['manger', 'senior', 'staff', 'help_desk'])
def setConcentration(request, pk):
    Con = Concentration.objects.get(id=pk)
    form = ConcentrationForm(instance=Con)
    if request.method == 'POST':
        form = ConcentrationForm(request.POST, instance=Con)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/concentration_form.html', context)


@login_required(login_url='login')
@manger_only
def equipmentPage(request):
    equipment = Equipment.objects.all()
    total_equipment = Equipment.objects.all().count()
    Corona = equipment.filter(department='Corona').count()
    EmergencyRoom = equipment.filter(department='Emergency room').count()
    Heart = equipment.filter(department='Heart').count()
    ENP = equipment.filter(department='ENP').count()
    Stock = equipment.filter(department='Stock').count()
    context = {
        'equipment': equipment,
        'total_equipment': total_equipment,
        'Corona': Corona,
        'EmergencyRoom': EmergencyRoom,
        'Heart': Heart,
        'ENP': ENP,
        'Stock': Stock,
    }
    return render(request, 'accounts/equipment.html', context)


@login_required(login_url='login')
@manger_only
def addEquipment(request):
    form = EquipForm
    if request.method == 'POST':
        form = EquipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/equipment/')
    context = {'form': form}
    return render(request, 'accounts/equipment_form.html', context)


@login_required(login_url='login')
@manger_only
def updateEquipment(request, pk):
    eq = Equipment.objects.get(id=pk)
    form = EquipForm(instance=eq)
    if request.method == 'POST':
        form = EquipForm(request.POST, instance=eq)
        if form.is_valid():
            form.save()
            return redirect('/equipment/')
    context = {'form': form}
    return render(request, 'accounts/equipment_form.html', context)


@login_required(login_url='login')
@manger_only
def deleteEquipment(request, pk):
    eq = Equipment.objects.get(id=pk)
    if request.method == 'POST':
        eq.delete()
        return redirect('/equipment/')
    context = {'eq': eq}
    return render(request, 'accounts/equipment_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['senior', 'staff', 'help_desk'])
def createRequest(request):
    form = ReqForm()
    if request.method == 'POST':
        form = ReqForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/request_form.html', context)

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
