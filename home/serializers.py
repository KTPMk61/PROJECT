from rest_framework import serializers
from .models import *

class acountSerializer(serializers.ModelSerializer):
    class Meta:
        model = acount
        fields = ('id','username','password')

class gradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = grade
        fields = ('id','idcls','name','subjectId')

class lecturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = lecturer
        fields = ('id','name','phone_mail','institute','birthday')

class lecturer_classSerializer(serializers.ModelSerializer):
    class Meta:
        model = lecturer_class
        fields = ('id','lecturerId','classid')

class pointSerializer(serializers.ModelSerializer):
    class Meta:
        model = point
        fields = ('id','studentId','classId','subjectId','point','point2')

class student_classSerializer(serializers.ModelSerializer):
    class Meta:
        model = student_class
        fields = ('id','classId','student')

class subjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = subject
        fields = ('id','subjectId','title','subject_code')

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = ('id','name','mssv','email','student_class')
