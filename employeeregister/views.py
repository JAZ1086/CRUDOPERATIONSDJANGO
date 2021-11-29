from django.shortcuts import redirect, render
from .models import *
from .form import *
# Create your views here.

def employeelist(request):
    listofempolyees = Employee.objects.all()
    # print(listofempolyees)
    return render(request,"employeeregister/employeelist.html",{
        "listofemployee" :listofempolyees
    })


def employeeform(request,id=0):
    #create an instance of form from the Employeeform class
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employeedata = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employeedata)
        return render(request,'employeeregister/employeeform.html',{
        'form':form
        })
    else :
        if id == 0 :
            form = EmployeeForm(request.POST)
        else:
            employeedata = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance=employeedata)
            print(form)
        if form.is_valid():
            form.save()
        return redirect('/employee/list')

def employeedelete(request,id):
    employeedata = Employee.objects.get(pk=id)
    employeedata.delete()
    return redirect('/employee/list')