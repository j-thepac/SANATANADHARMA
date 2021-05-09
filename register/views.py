from django.shortcuts import render,HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserFrom
from django.contrib import messages
# Create your views here.

def register(request):
    form = CreateUserFrom()
    context = {'form': form}
    if (request.method == "GET"):
        return render(request,"register.html",context)


    elif (request.method=="POST"):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, 'The form is valid.')
            return render(request, "login.html")
        else:
            # print (form.errors)
            # return render(request, "register.html", {'form': form.errors.values})
            return HttpResponse(form.errors.values())
            # return render(request, 'users/contact.html', context={'form': form})
            # messages.error(request, 'The form is invalid.')
            # print(form.errors)
            # return HttpResponse("something went wrong")


