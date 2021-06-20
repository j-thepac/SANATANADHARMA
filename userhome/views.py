from django.shortcuts import render
from django.shortcuts import HttpResponse,render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages

# Create your views here.


def user_home(request):
    if not request.user.is_authenticated:
        return HttpResponse("User not logged in")
    elif request.method == "POST":
        print("hi")
        return logoutUser(request)
    else:
        userdetails={"username":request.user.username}
        return render(request, "user_dashboard.html",userdetails)



def logoutUser(request):
    logout(request)
    return HttpResponse("User logget out")
    # return redirect("login")

