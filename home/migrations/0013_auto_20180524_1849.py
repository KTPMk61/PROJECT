# Generated by Django 2.0.4 on 2018-05-24 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_logincheck'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturer',
            name='phone_mail',
            field=models.CharField(max_length=50),
        ),
    ]