from django.shortcuts import render
from django.shortcuts import HttpResponse,render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
# import SANATANADHARMA_MAIN.userhome
from django.urls import reverse


def loginPage(request):
    if ( request.user.is_authenticated):return redirect('user_home')
    if (request.method=="POST"):
        username=request.POST.get("username")
        password=request.POST.get("password")
        user = authenticate(username=username,password=password)
        if (user is not None):
            login(request,user)
            return redirect('user_home')
            # return render(request,"index.html")
        else:
            messages.info(request,'Username or Password incorrect')

    return render(request,"login.html")

# def logoutUser(request):
#     logout(request)
#     return redirect("login")