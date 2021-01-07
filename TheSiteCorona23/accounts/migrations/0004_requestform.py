# Generated by Django 3.1.4 on 2021-01-07 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_equipment_date_registered'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=264, null=True)),
                ('name_of_req', models.CharField(choices=[('Add Equipment', 'Add Equipment'), ('Add Beds', 'Add Beds')], max_length=264, null=True)),
                ('description', models.TextField(max_length=5400, null=True)),
                ('date_registered', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]