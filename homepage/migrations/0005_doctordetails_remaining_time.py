# Generated by Django 2.2.1 on 2019-06-04 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20190604_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctordetails',
            name='remaining_time',
            field=models.IntegerField(null=True),
        ),
    ]
