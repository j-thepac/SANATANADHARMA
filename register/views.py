from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserFrom
from django.contrib import messages



def register(request):
    form = CreateUserFrom()
    if (request.method=="POST"):
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user= form.cleaned_data.get('username')
            messages.success(request,"Account was created for "+user)
            return redirect("loginPage") #     return HttpResponse(form.errors.values())

    context = {'form': form}
    return render(request,"register.html",context)





