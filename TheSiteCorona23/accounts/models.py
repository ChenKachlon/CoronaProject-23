from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Bed(models.Model):
    DEP = (
        ('Corona', 'Corona'),
        ('ENP', 'ENP'),
        ('Heart', 'Heart'),
        ('Emergency room', 'Emergency room'),
    )
    name = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True, choices=DEP)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    room_number = models.IntegerField(null=True)
    # amount= models.IntegerField(null=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Ventilator(models.Model):
    DEP = (
        ('Corona', 'Corona'),
        ('ENP', 'ENP'),
        ('Heart', 'Heart'),
        ('Emergency room', 'Emergency room'),
    )
    name = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=200, null=True, choices=DEP)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    room_number = models.IntegerField(null=True)
    ventilator_number = models.IntegerField(null=True)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Patient(models.Model):
    STATUS = (
        ('mildly ill', 'mildly ill'),
        ('medium ill', 'medium ill'),
        ('seriously ill', 'seriously ill'),
        ('dying', 'dying'),
    )
    VEN = (
        ('YES', 'YES'),
        ('NO', 'NO'),
    )
    DEP = (
        ('Corona', 'Corona'),
        ('ENP', 'ENP'),
        ('Heart', 'Heart'),
        ('Emergency room', 'Emergency room'),
    )
    name = models.CharField(max_length=200, null=True)
    ID = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    department = 'Corona' # for temp check
    # department = models.CharField(max_length=200, null=True, choices=DEP, default=None)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    need_ven = models.CharField(max_length=200, null=True, choices=VEN)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class Concentration(models.Model):
    Amount = models.IntegerField(null=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.Amount)


class Equipment(models.Model):
    DEP = (
        ('Corona', 'Corona'),
        ('ENP', 'ENP'),
        ('Heart', 'Heart'),
        ('Emergency room', 'Emergency room'),
        ('Stock', 'Stock'),
    )
    name = models.CharField(max_length=200, null=True)
    department = models.CharField(max_length=264, null=True, choices=DEP)
    date_registered = models.DateTimeField(auto_now_add=True, null=True)
    objects = models.Manager()

    def __str__(self):
        return self.name


class RequestForm(models.Model):
    OPTION = {
        ('Add Equipment', 'Add Equipment'),
        ('Add Beds', 'Add Beds'),
    }
    name = models.CharField(max_length=264, null=True)
    request = models.CharField(max_length=264, null=True, choices=OPTION)
    description = models.TextField(max_length=264, null=True)
    date_registered = models.DateTimeField(auto_now_add=True, null=True)
    objects = models.Manager()


class Department(models.Model):
    DEP = (
        ('Corona', 'Corona'),
        ('ENP', 'ENP'),
        ('Heart', 'Heart'),
        ('Emergency room', 'Emergency room'),
    )
    department = models.CharField(max_length=200, null=True, choices=DEP, default='Corona')
    objects = models.Manager()

    def __str__(self):
        return self.department
