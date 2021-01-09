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


# Create our views here.

@unauthenticated_user
def registerPage(request):
    """Website registration function and reload him"""
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
    """Website login function and reload him"""
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
    """Website logout function"""
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@manger_only
def home(request):
    """function that fill the fields of home page- in dashboard part of the website,and reload him """
    dep = Department.objects.all()
    pati = Patient.objects.all()
    bedi = Bed.objects.all()
    ven = Ventilator.objects.all()
    all_beds = bedi.count()
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
        'beds': all_beds,
        'Ventilator': xx,
        'patients': pati,
        'freeBeds': free_beds,
        'departments': dep
    }
    return render(request, 'accounts/dashboard.html', context)


@login_required(login_url='login')
def departmentPage(request, pk_dep):
    dep = Department.objects.get(department=pk_dep)
    dep_name = dep.department
    concentration = Concentration.objects.get(name=dep_name)
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
    context = {'department': dep_name, 'dep_beds': dep_beds, 'Beds': all_beds,
               'Ventilator': dep_ven, 'patients': patient, 'concentration': concentration,
               'freeBeds': free_beds, 'Ventilators': all_ven}
    return render(request, 'accounts/department.html', context)


@login_required(login_url='login')
@manger_only
def patients(request):
    """function that fill the fields of patients page of the website,and reload him"""
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
    """function that fill the fields of beds page of the website,and reload him"""
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
    """function that fill the fields of ventilators page of the website,and reload him"""
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
    """function that add a new patient to patients page/home page of the website and update the database,and reload the page"""
    form = PatientForm()
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/patients/')
    context = {'form': form}
    return render(request, 'accounts/patients_form.html', context)


@login_required(login_url='login')
@manger_only
def updatePatient(request, pk):
    """function that update a status of exist patient and update the database,and reload the page"""
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
    """function that remove patient from patients page/home page of the website and update the database,and reload the page"""
    patient = Patient.objects.get(id=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('/patients/')
    context = {'patient': patient}
    return render(request, 'accounts/delete_patient.html', context)


@login_required(login_url='login')
@manger_only
def addBeds(request):
    """function that add a new bed to beds page of the website and update the database,and reload the page """
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
    """function that update a fields of exist bed and update the database,and reload the page """
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
    """function that remove bed from beds page of the website and update the database,and reload the page """
    bed = Bed.objects.get(id=pk)
    if request.method == 'POST':
        bed.delete()
        return redirect('/beds/')
    context = {'bed': bed}
    return render(request, 'accounts/beds_form.html', context)


@login_required(login_url='login')
@manger_only
def addVen(request):
    """function that add a new ventilator to ventilators page of the website and update the database,and reload the page """
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
    """function that update a fields of exist ventilator and update the database,and reload the page """
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
    """function that remove ventilator from ventilators page of the website and update the database,and reload the page """
    ven = Ventilator.objects.get(id=pk)
    if request.method == 'POST':
        ven.delete()
        return redirect('/ventilators/')
    context = {'ven': ven}
    return render(request, 'accounts/ventilators_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['manger', 'senior', 'staff', 'help_desk'])
def setConcentration(request, pk):
    """A function that determines the maximum population in the hospital and in each department in the hospital and update the database,and reload the page """
    Con = Concentration.objects.get(name=pk)
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
    """function that fill the fields of equipment page of the website and update the database,and reload the page """
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
    """function that add a new medical equipment to equipment page of the website and update the database,and reload the page """
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
    """function that update a fields of exist equipment and update the database,and reload the page """
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
    """function that remove equipment from equipment page of the website and update the database,and reload the page """
    eq = Equipment.objects.get(id=pk)
    if request.method == 'POST':
        eq.delete()
        return redirect('/equipment/')
    context = {'eq': eq}
    return render(request, 'accounts/equipment_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['senior', 'staff', 'help_desk'])
def createRequest(request):
    """a function that create a new request and update the database,and reload the page"""
    form = ReqForm()
    if request.method == 'POST':
        form = ReqForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/request_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['senior', 'staff', 'help_desk'])
def createReport(request):
    """a function that create a new report and update the database,and reload the page"""
    form = RepForm
    if request.method == 'POST':
        form = RepForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/report_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['manager', 'help_desk'])
def ReqANDRep(request):
    """function that fill the fields of requests&reports page of the website,and reload him """
    req = RequestForm.objects.all()
    rep = ReportForm.objects.all()
    context = {'requests': req, 'reports': rep}
    return render(request, 'accounts/request&report.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['manager', 'help_desk'])
def approveRequest(request, pk):
    """a function that approve a exist request and update the database,and reload the page"""
    req = RequestForm.objects.get(id=pk)
    obj = req.request
    if request.method == 'POST':
        req.delete()
        if obj == 'Add Beds':
            return redirect('/beds/')
        return redirect('/equipment/')
    context = {'req': req}
    return render(request, 'accounts/request_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['manager', 'help_desk'])
def rejectRequest(request, pk):
    """a function that reject a exist request and update the database,and reload the page"""
    req = RequestForm.objects.get(id=pk)
    if request.method == 'POST':
        req.delete()
        return redirect('/')
    context = {'req': req}
    return render(request, 'accounts/request_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['manager', 'help_desk'])
def deleteReport(request, pk):
    """a function that delete a exist report and update the database,and reload the page"""
    rep = ReportForm.objects.get(id=pk)
    if request.method == 'POST':
        rep.delete()
        return redirect('/')
    context = {'rep': rep}
    return render(request, 'accounts/report_form.html', context)
