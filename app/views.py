from django.shortcuts import render

# Create your views here.

def cricketer(request):
    return render(request,'cricketer.html')