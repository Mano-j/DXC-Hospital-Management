# Generated by Django 2.2.1 on 2019-06-05 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20190605_0616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctordetails',
            name='remaining_time',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
