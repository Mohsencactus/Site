from django.shortcuts import render,HttpResponse
from .models import Intro

def home(request):
    data = {"Intros" : Intro.objects.all , "Loged" : request.user.is_authenticated }
    return render(request,'home.html',data)
