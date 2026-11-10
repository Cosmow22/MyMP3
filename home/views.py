from django.shortcuts import render

def home(request):
    if request.headers.get("HX-Request"):
        return render(request, "home/home_content.html", {
        'active_page': 'home'
    })

    return render(request, "home/home.html", {
        'active_page': 'home'
    })