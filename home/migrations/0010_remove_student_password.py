# Generated by Django 2.0.5 on 2018-05-19 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_point_classid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='password',
        ),
    ]
