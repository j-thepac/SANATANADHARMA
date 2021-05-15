from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
from django.shortcuts import HttpResponse,render
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages




def loginPage(request):
    if (request.method=="POST"):
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username,password=password)
        if (user is not None):
            login(request,user)
            return render(request,"index.html")
        else:
            messages.info(request,'Username or Password incorrect')

    return render(request,"login.html")