from django.shortcuts import render
from django.http import HttpResponse

def Say_Hello(request):
    return render(request, 'hello.html')