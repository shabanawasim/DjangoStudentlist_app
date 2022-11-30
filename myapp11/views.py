from django.shortcuts import render
from urllib import request
from django.contrib import messages
from .models import StudentTable
# Create your views here.
def home(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['dept']
        email=request.POST['email']
        phno=request.POST['num']
        addr=request.POST['addr']
        ins=StudentTable(name=name, Department=dept, Email=email, MObile=phno, Address=addr)
        ins.save()
        messages.success(request, 'Form submitted successfully!')
        alltasks=StudentTable.objects.filter()
        context={'tasks':alltasks}
        return render(request, 'myapp11/home.html', context)
    else:
        alltasks=StudentTable.objects.all()
        context={'tasks':alltasks}
        return render(request, 'myapp11/home.html', context)
    