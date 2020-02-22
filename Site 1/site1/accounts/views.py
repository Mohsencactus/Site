from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm,UserRegisterForm
from .excel import exs
from django.contrib.auth import authenticate,get_user_model,login,logout

def loginpage(request):
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/accounts/')
    context = {'form': form}
    return render(request, "login.html", context)

def registerpage(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect('/accounts')
    context = {'form': form}
    return render(request, "signup.html", context)

def logoutpage(request):
    logout(request)
    return redirect('/')


@login_required
def accounts(request):
    excels = exs()
    return render(request,'accounts.html',excels.data)
