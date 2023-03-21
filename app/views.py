from django.shortcuts import render

# Create your views here.
def specificstatic(request):
    return render(request,'specific_static.html')