from django.shortcuts import render

def welcome(request):
    return render(request, "welcome/index.html")