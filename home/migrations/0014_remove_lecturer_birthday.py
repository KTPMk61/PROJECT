# Generated by Django 2.0.4 on 2018-05-24 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20180524_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lecturer',
            name='birthday',
        ),
    ]
