from django.shortcuts import render
from tasks.models import Task


def home(request):
    task =Task.objects.all()
    return render(request,'home.html',{'data':task})