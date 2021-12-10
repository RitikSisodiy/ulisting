from django.shortcuts import render

# Create your views here.
def dashboard(request):
    res = {}
    return render(request,'userpanel/dashboard.html',res)