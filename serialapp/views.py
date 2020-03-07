from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    data=StudentName.objects.all
    if request.method=='POST':
        name=request.POST['name']
        StudentName.objects.create(name=name)
    return render(request,'index.html',{'data':data})

def Delete_name(request,sid,option):
    data=StudentName.objects.filter(id=sid).first()
    if option=='Delete':
        data.delete()
        return redirect('index')
    return render(request,'index.html',{'data':data})