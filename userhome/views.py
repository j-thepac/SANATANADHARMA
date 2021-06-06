from django.shortcuts import render
from django.shortcuts import HttpResponse,render,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages

# Create your views here.


def user_home(request):
    if (not request.user.is_authenticated): return HttpResponse("User not logged in")
    if (request.method == "POST"):
        # logoutbutton = request.POST.get('Logout')
        # if logoutbutton:
        print("hi")
        logoutUser(request)
    return render(request, "userhome.html")



def logoutUser(request):
    logout(request)
    return HttpResponse("User logget out")
    # return redirect("login")