from django.db import models
class acount(models.Model):
    username= models.CharField(max_length=50)
    password = models.CharField(max_length=50)
class grade(models.Model):
    idcls=models.IntegerField(default=0)
    name= models.CharField(max_length=30)
    subjectId= models.IntegerField(default=0)
class lecturer(models.Model):
    name= models.CharField(max_length=40)
    phone_mail=models.CharField(max_length=40)
    institute= models.CharField(max_length=40)
    birthday= models.CharField(max_length=40)
class lecturer_class(models.Model):
    lecturerId=models.IntegerField(default=0)
    classid=models.IntegerField(default=0)
class point(models.Model):
    studentId=models.IntegerField()
    subjectId=models.IntegerField()
    classId=models.IntegerField()
    point= models.FloatField(null=True)
    point2=models.FloatField(null=True)
class student_class(models.Model):
    classId=models.IntegerField(default=0)
    student=models.IntegerField(default=0)
class subject(models.Model):
    subjectId=models.IntegerField(default=0)
    title= models.CharField(max_length=40)
    subject_code=models.CharField(max_length=40)
class student(models.Model):
    name = models.CharField(max_length=50)
    mssv= models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    student_class = models.CharField(max_length=50)
# Create your models here.
