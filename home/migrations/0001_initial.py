# Generated by Django 2.0.5 on 2018-05-15 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcls', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=30)),
                ('subjectId', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='lecturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('phone_mail', models.CharField(max_length=40)),
                ('institute', models.CharField(max_length=40)),
                ('birthday', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='lecturer_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lecturerId', models.CharField(max_length=40)),
                ('classid', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('studentId', models.IntegerField()),
                ('subjectId', models.IntegerField()),
                ('point', models.FloatField()),
                ('point2', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mssv', models.CharField(max_length=40)),
                ('username', models.CharField(max_length=40)),
                ('student_class', models.CharField(max_length=40)),
                ('birthday', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='student_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classId', models.IntegerField(default=0)),
                ('student', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subjectId', models.IntegerField(default=0)),
                ('title', models.CharField(max_length=40)),
                ('subject_code', models.CharField(max_length=40)),
            ],
        ),
    ]
