# Generated by Django 3.1.7 on 2021-04-11 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listrequests', '0002_charity_request_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charity_request',
            name='created_by',
        ),
    ]
