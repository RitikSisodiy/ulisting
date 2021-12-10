from django.shortcuts import render

# Create your views here.
def listing(request):
    res = {}
    return render(request,'ulisting/listings_grid_full_width.html', res)