# Generated by Django 3.1.4 on 2021-01-06 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210105_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bed',
            name='name',
            field=models.CharField(max_length=200, null='UNKNOWN'),
        ),
    ]
