# Generated by Django 2.2.15 on 2020-08-24 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='user_name',
        ),
    ]
