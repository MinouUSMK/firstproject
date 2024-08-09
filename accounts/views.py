from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    form=UserCreationForm(request.POST or None)
    if form.is_valid():
        user_obj=form.save()
        return redirect('/accounts/login')
    context={'form':form}
    return render(request,'register.html',context)
    

def login_view(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is None:
            context={
                'erroe':'invalid username or password'
            }
            return render(request,'login.html',context)
        login(request,user)
        return redirect('/blog')

    return render(request,'login.html',{})