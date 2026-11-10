from django.shortcuts import render

def home(request):
    if request.headers.get("HX-Request"):
        return render(request, "home/home_content.html")

    return render(request, "home/home.html")