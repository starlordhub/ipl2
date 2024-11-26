from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1>captain of RCB is Virat Kohli</h1>')

def vicecaptain(request):
    return HttpResponse('<h1>vice captain of csk is faf duplesis</h1>')
