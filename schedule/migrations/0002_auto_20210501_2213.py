# Generated by Django 3.2 on 2021-05-01 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='check_in_time',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='check_out_time',
        ),
    ]
