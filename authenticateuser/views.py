from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login , logout
# Create your views here.
def signin(request):
    res= {}
    return render(request,'athenticateuser/')
def signout(request):
    logout(request)
    return redirect('home')