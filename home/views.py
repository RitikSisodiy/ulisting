from django.shortcuts import render

# Create your views here.
def index(request):
    res = {}
    return render(request,'home/index.html',res)