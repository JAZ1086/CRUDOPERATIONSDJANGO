from django.urls import path 

from . import views

urlpatterns = [
    path('form',views.employeeform,name="employeeform"),
    path('<int:id>/',views.employeeform,name="employeeupdate"),
    path('list',views.employeelist,name="employeelist"),
    path('',views.employeedelete,name="employeedelete"),
    path('delete/<int:id>',views.employeedelete,name="employeedelete")
]