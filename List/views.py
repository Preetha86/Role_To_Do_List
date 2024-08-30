from django.shortcuts import render

def First(request):
    return render(request,'First.html')

def insert(request):
    return render(request,'insert.html')