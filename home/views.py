from django.shortcuts import render,render_to_response,redirect
from .models import *
from .form import *
from django.forms.models import modelformset_factory
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import *
class LoginCheck:
    check=-1
def home(request):
    if LoginCheck.check==-1:
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user = form.cleaned_data['username']
                password = form.cleaned_data['password']
                data = acount.objects.all()
                data1= lecturer.objects.all()
                data2= student.objects.all()
                for s in data:
                    if s.username == user and s.password == password:
                        for s1 in data1:
                            if user==s1.phone_mail :
                                temp= lecturer.objects.get(id=s1.id)
                                acc= acount.objects.get(username=user)
                                LoginCheck.check=acc.id
                                return render(request, 'pages/teacher.html', {'teacher':temp,'acc':acc})
                        for s2 in data2:
                            if user==s2.mssv:
                                temp1= student.objects.get(id=s2.id)
                                acc1 = acount.objects.get(username=user)
                                LoginCheck.check=acc1.id
                                return render(request, 'pages/student.html', {'student': temp1,'acc':acc1})
                return render(request, 'pages/fail1.html')
        return render(request, 'pages/login.html', {'form': form})
    else:
        temp2 = lecturer.objects.get(id=LoginCheck.check)
        acc2 = acount.objects.get(username=temp2.phone_mail)
        return render(request, 'pages/teacher.html', {'teacher':temp2,'acc':acc2})
def register(request):
    form = TeacherRegisterForm()
    if request.method == 'POST':
        form = TeacherRegisterForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['email']
            data = acount.objects.all()
            for s in data:
                if s.username== user:
                    return render(request,'pages/fail.html')
            form.save()
            return render(request, 'pages/sucess.html')
    return render(request, 'pages/teacherreg.html', {'form': form})
def studentinf(request,idA,idS):
    if LoginCheck.check==idA:
        a = acount.objects.get(id=idA)
        s= student.objects.get(id=idS)
        return render(request,'pages/studentinf.html',{'acc':a,'student':s})
    return HttpResponseRedirect('/')
def student_home(request,idA,idS):
    if LoginCheck.check==idA:
        a = acount.objects.get(id=idA)
        s= student.objects.get(id=idS)
        return render(request,'pages/student.html',{'acc':a,'student':s})
    return HttpResponseRedirect('/')
def teacherview(request,idA,idS):
    if LoginCheck.check==idA:
        a = acount.objects.get(id=idA)
        s = student.objects.get(id=idS)
        cls = student_class.objects.all()
        lectcls = lecturer_class.objects.all()
        teach = lecturer.objects.all()
        return render(request, 'pages/teacherinf.html', {'acc': a, 'student': s,'stclass':cls,'lectclass':lectcls,'teacher':teach})
    return HttpResponseRedirect('/')
def viewclass(request,idA,idS):
    if LoginCheck.check==idA:
        a = acount.objects.get(id=idA)
        s = student.objects.get(id=idS)
        cls = student_class.objects.all()
        clsname = grade.objects.all()
        return render(request, 'pages/viewclass.html', {'acc': a, 'student': s,'stcls':cls,'clsname':clsname})
    return HttpResponseRedirect('/')
def memcls(request,idA,idS,idC):
    if LoginCheck.check==idA:
        a = acount.objects.get(id=idA)
        s = student.objects.get(id=idS)
        c = grade.objects.get(idcls=idC)
        data= student.objects.all()
        cls = student_class.objects.all()
        return render(request, 'pages/viewmem.html', {'acc': a, 'student': s,'class':c ,'stcls': cls,'data':data})
    return HttpResponseRedirect('/')
def teacher(request,idA,idT):
    if LoginCheck.check==idA:
        a = acount.objects.get(id=idA)
        t = lecturer.objects.get(id=idT)
        return render(request, 'pages/teacher.html', {'acc': a, 'teacher': t})
    return HttpResponseRedirect('/')
def viewinfteacher(request,idA,idT):
    if LoginCheck.check==idA:
        a = acount.objects.get(id=idA)
        t = lecturer.objects.get(id=idT)
        return render(request,'pages/viewinf.html',{'acc':a,'teacher':t})
    return HttpResponseRedirect('/')
def creatclass(request,idA,idT):
    if LoginCheck.check==idA:
        idclass = 0
        check = 0
        idclass1 = 1
        a = acount.objects.get(id=idA)
        t = lecturer.objects.get(id=idT)
        st = student.objects.all()
        form = CreatClass()
        clas = grade.objects.all()
        data = subject.objects.all()
        if request.method =='POST':
            form = CreatClass(request.POST)
            if form.is_valid():
                subname = form.cleaned_data['subname']
                subcode = form.cleaned_data['subcode']
                clsname = form.cleaned_data['classname']
                for s in clas:
                    check=check+1
                    if s.name != clsname:
                        idclass=idclass+1
                if check==idclass and check!=0:
                    for s1 in clas:
                        dclass1 = idclass1 + 1
                    for s2 in data:
                        if s2.subject_code == subcode:
                            subjectId = s2.subjectId
                    sub = grade(idcls=idclass1, name=clsname, subjectId=subjectId)
                    sub.save()
                    teacher_class = lecturer_class(classid=idclass1,lecturerId=idT)
                    teacher_class.save()
                    gr= grade.objects.get(idcls=idclass1)
                    return render(request,'pages/creatsucess.html',{'acc': a, 'teacher': t,'class':gr,'subject':sub})
                if check==0:
                    for s2 in data:
                        if s2.subject_code == subcode:
                            subjectId= s2.subjectId
                    sub = grade(idcls=idclass1, name=clsname, subjectId=subjectId)
                    sub.save()
                    teacher_class = lecturer_class(classid=idclass1, lecturerId=idT)
                    teacher_class.save()
                    gr = grade.objects.get(idcls=idclass1)
                    cls = student_class.objects.all()
                    return render(request, 'pages/creatsucess.html', {'acc': a, 'teacher': t,'class':gr,'subject':sub})
                if idclass<check :
                    return render(request,'pages/failcreate.html',{'acc': a, 'teacher': t,'form':form})
        return render(request, 'pages/creatclass.html', {'acc': a, 'teacher': t,'form':form})
    return HttpResponseRedirect('/')
def addmem(request,idA,idT,idC,idS):
    if LoginCheck.check==idA:
        check=0
        form = AddMem()
        a = acount.objects.get(id=idA)
        t = lecturer.objects.get(id=idT)
        st = student.objects.all()
        gr = grade.objects.get(idcls=idC)
        cls = student_class.objects.all()
        if request.method =='POST':
            form = AddMem(request.POST)
            if form.is_valid():
                mssv = form.cleaned_data['mssv']
                for s in st:
                    if s.mssv==mssv :
                        check=1
                        temp=student.objects.get(id=s.id)
                if check!=0:
                    for s1 in cls:
                        if s1.classId == idC:
                            if s1.student == temp.id:
                                return render(request, 'pages/addmemfail.html',{'acc': a, 'teacher': t, 'student': st, 'class': gr, 'stcls': cls, 'form': form})
                    mem = student_class(classId=idC, student=temp.id)
                    mem.save()
                    score=point(studentId=temp.id,subjectId=idS,classId = idC)
                    score.save()
                    return render(request, 'pages/addmem.html',{'acc': a, 'teacher': t, 'student': st, 'class': gr, 'stcls': cls, 'form': form,'temp': temp})
                else :
                    return render(request,'pages/addmemfail1.html',{'acc': a, 'teacher': t, 'student': st, 'class': gr, 'stcls': cls, 'form': form})
        return render(request, 'pages/addmem.html',{'acc': a, 'teacher': t, 'student': st, 'class': gr, 'stcls': cls, 'form': form})
    return HttpResponseRedirect('/')
def updatescore(request,idA,idT,idC,idS):
    if LoginCheck.check==idA:
        a = acount.objects.get(id=idA)
        t = lecturer.objects.get(id=idT)
        st = student.objects.all()
        gr = grade.objects.get(idcls=idC)
        cls = student_class.objects.all()
        score = point.objects.filter(classId=idC,subjectId=idS)
        total = point.objects.all()
        Update = modelformset_factory(point,fields=["point","point2", ], labels={'point': 'Điểm Giữa Kì','point2':'Điểm Cuối Kì'}, extra=0)
        formset = Update(request.POST or None,queryset=point.objects.filter(classId=idC,subjectId=idS))
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.user = request.user
                instance.save()
        return render(request, 'pages/update.html', {'acc': a, 'teacher':t,'score':score,'student': st, 'class': gr, 'stcls': cls, 'formset': formset,'total':total})
    return HttpResponseRedirect('/')
def viewclasst(request,idA,idT):
    if LoginCheck.check==idA:
        a = acount.objects.get(id=idA)
        t = lecturer.objects.get(id=idT)
        cls = lecturer_class.objects.all()
        clsname = grade.objects.all()
        sub = subject.objects.all()
        return render(request, 'pages/viewclasst.html', {'acc': a, 'teacher':t, 'stcls': cls, 'clsname': clsname,'subjects':sub})
    return HttpResponseRedirect('/')
def logout(request):
    LoginCheck.check=-1
    return HttpResponseRedirect('/')
#REST API Controller

#List (GET + POST)
@csrf_exempt
def acount_list(request):
    if request.method == 'GET':
        obj = acount.objects.all()
        serializer = acountSerializer(obj, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = acountSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def grade_list(request):
    if request.method == 'GET':
        obj = grade.objects.all()
        serializer = gradeSerializer(obj, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = gradeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def lecturer_list(request):
    if request.method == 'GET':
        obj = lecturer.objects.all()
        serializer = lecturerSerializer(obj, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = lecturerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def lecturer_class_list(request):
    if request.method == 'GET':
        obj = lecturer_class.objects.all()
        serializer = lecturer_classSerializer(obj, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = lecturer_classSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def point_list(request):
    if request.method == 'GET':
        obj = point.objects.all()
        serializer = pointSerializer(obj, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = pointSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def student_class_list(request):
    if request.method == 'GET':
        obj = student_class.objects.all()
        serializer = student_classSerializer(obj, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = student_classSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def subject_list(request):
    if request.method == 'GET':
        obj = subject.objects.all()
        serializer = subjectSerializer(obj, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = subjectSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def student_list(request):
    if request.method == 'GET':
        obj = student.objects.all()
        serializer = studentSerializer(obj, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = studentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

#Detail (GET + PUT + DELETE)
@csrf_exempt
def acount_detail(request, pk):
    try:
        obj = acount.objects.get(pk=pk)
    except acount.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = acountSerializer(obj)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = acountSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

@csrf_exempt
def grade_detail(request, pk):
    try:
        obj = grade.objects.get(pk=pk)
    except grade.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = gradeSerializer(obj)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = gradeSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

@csrf_exempt
def lecturer_detail(request, pk):
    try:
        obj = lecturer.objects.get(pk=pk)
    except lecturer.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = lecturerSerializer(obj)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = lecturerSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

@csrf_exempt
def lecturer_class_detail(request, pk):
    try:
        obj = lecturer_class.objects.get(pk=pk)
    except lecturer_class.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = lecturer_classSerializer(obj)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = lecturer_classSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

@csrf_exempt
def point_detail(request, pk):
    try:
        obj = point.objects.get(pk=pk)
    except point.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = pointSerializer(obj)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = pointSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

@csrf_exempt
def student_class_detail(request, pk):
    try:
        obj = student_class.objects.get(pk=pk)
    except student_class.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = student_classSerializer(obj)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = student_classSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

@csrf_exempt
def subject_detail(request, pk):
    try:
        obj = subject.objects.get(pk=pk)
    except subject.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = subjectSerializer(obj)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = subjectSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)

@csrf_exempt
def student_detail(request, pk):
    try:
        obj = student.objects.get(pk=pk)
    except student.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = studentSerializer(obj)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = studentSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        obj.delete()
        return HttpResponse(status=204)