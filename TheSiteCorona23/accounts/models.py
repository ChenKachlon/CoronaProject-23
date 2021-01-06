from django.db import models

# Create your models here.


class Bed(models.Model):

    DEP=(
        ('Corona','Corona'),
        ('ENP','ENP'),
        ('Heart', 'Heart'),
        ('Emergency room', 'Emergency room'),
    )
    name=models.CharField(max_length=200,null=True)
    department=models.CharField(max_length=200,null=True,choices=DEP)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    room_number = models.IntegerField(null=True)
   # amount= models.IntegerField(null=True)
    objects = models.Manager()

    def __str__(self):
        return self.name



class Ventilator(models.Model):
    DEP=(
        ('Corona','Corona'),
        ('ENP','ENP'),
        ('Heart', 'Heart'),
        ('Emergency room', 'Emergency room'),
    )
    name=models.CharField(max_length=200,null=True)
    department=models.CharField(max_length=200,null=True,choices=DEP)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    room_number=models.IntegerField(null=True)
    ventilator_number = models.IntegerField(null=True)

    objects=models.Manager()

    def __str__(self):
        return self.name


class Patient (models.Model):
    STATUS=(
            ('mildly ill','mildly ill'),
            ('medium ill' ,'medium ill'),
            ('seriously ill','seriously ill'),
            ('dying','dying'),
            )
    VEN=(
        ('YES','YES'),
        ('NO','NO'),
    )
    DEP=(
        ('Corona','Corona'),
        ('ENP','ENP'),
        ('Heart', 'Heart'),
        ('Emergency room', 'Emergency room'),
    )
    name=models.CharField(max_length=200,null=True)
    ID=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=200,null=True,choices=STATUS)
    need_ven=models.CharField(max_length=200,null=True,choices=VEN)
    date_created=models.DateTimeField(auto_now_add=True,null=True)
    objects=models.Manager()


    def __str__(self):
        return self.name
