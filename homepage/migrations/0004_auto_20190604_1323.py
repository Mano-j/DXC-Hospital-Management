# Generated by Django 2.2.1 on 2019-06-04 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20190604_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdetails',
            name='doctorDetails',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='homepage.DoctorDetails'),
        ),
    ]
