# Generated by Django 3.1.4 on 2021-01-07 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_equipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='date_registered',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
