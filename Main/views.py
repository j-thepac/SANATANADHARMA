from django.http import request
from django.shortcuts import HttpResponse,render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']

def index(request):
    return render(request,'index2.html')
    
def events(request):
    return render(request,'events.html')

def contact(request):
    return render(request,'contact.html')

def loginPage(request):
    if ( request.user.is_authenticated):return redirect('user_home')
    if (request.method=="POST"):
        username=request.POST.get("username")
        password=request.POST.get("password")
        print("hi")
        user = authenticate(username=username,password=password)
        if (user is not None):
            login(request,user)
            return redirect('user_home')
            # return render(request,"index.html")
        else:
            messages.info(request,'Username or Password incorrect')
    return render(request,"login.html")

def register(request):
    form = CreateUserForm()
    if (request.method=="POST"):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user= form.cleaned_data.get('username')
            messages.success(request,"Account was created for "+user)
            return redirect("login") #     return HttpResponse(form.errors.values())

    context = {'form': form}
    return render(request,"register.html",context)

def user_home(request):
    if not request.user.is_authenticated:
        return HttpResponse("User not logged in")
    elif request.method == "POST":
        print("hi")
        return logoutUser(request)
    else:
        userdetails={"username":request.user.username}
        return render(request, "dashboard.html",userdetails)

def logoutUser(request):
    logout(request)
    return HttpResponse("User logget out") 
    # return redirect("login")

