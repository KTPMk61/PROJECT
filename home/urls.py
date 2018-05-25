from django.urls import path
from . import views
urlpatterns=[
    path('',views.home),
    path('register/',views.register),
    path('student_home/<int:idA>/<int:idS>/',views.student_home),
    path('studentinf/<int:idA>/<int:idS>/',views.studentinf),
    path('teacherview/<int:idA>/<int:idS>/',views.teacherview),
    path('viewclass/<int:idA>/<int:idS>/',views.viewclass),
    path('memcls/<int:idA>/<int:idS>/<int:idC>',views.memcls),
    path('viewinft/<int:idA>/<int:idT>/',views.viewinfteacher),
    path('teacher/<int:idA>/<int:idT>/',views.teacher),
    path('creatclass/<int:idA>/<int:idT>/',views.creatclass),
    path('addmem/<int:idA>/<int:idT>/<int:idC>/<int:idS>/',views.addmem),
    path('updatescore/<int:idA>/<int:idT>/<int:idC>/<int:idS>/',views.updatescore),
    path('viewclasst/<int:idA>/<int:idT>/',views.viewclasst),
    path('api/acount',views.acount_list),
    path('api/grade',views.grade_list),
    path('api/lecturer',views.lecturer_list),
    path('api/lecturer_class',views.lecturer_class_list),
    path('api/point',views.point_list),
    path('api/student_class',views.student_class_list),
    path('api/subject',views.subject_list),
    path('api/student',views.student_list),
    path('api/acount/<int:pk>',views.acount_detail),
    path('api/grade/<int:pk>',views.grade_detail),
    path('api/lecturer/<int:pk>',views.lecturer_detail),
    path('api/lecturer_class/<int:pk>',views.lecturer_class_detail),
    path('api/point/<int:pk>',views.point_detail),
    path('api/student_class/<int:pk>',views.student_class_detail),
    path('api/subject/<int:pk>',views.subject_detail),
    path('api/student/<int:pk>',views.student_detail),
    path('logout',views.logout),
    path('viewpoint/<int:idA>/<int:idS>/',views.view_point)
]