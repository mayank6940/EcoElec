from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    return render(request,"index.html")


def services(request):
    return render(request,"service.html")

def rewards(request):
    return render(request,"reward.html")

def contacts(request):
    return render(request,"contact.html")