from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def captain(request):
    return HttpResponse('<h1>captain of mi is Rohit Sharma</h1>')

def vicecaptain(request):
    return HttpResponse('<h1><marquee>vice captain of mi is Hardik Pandya</marquee></h1>')
