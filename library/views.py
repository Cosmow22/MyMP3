from django.shortcuts import render

from music.models import Music

def library(request):
    if not request.user.is_authenticated:
        if request.headers.get("HX-Request"):
            return render(request, "account/login.html", {
                "next": request.path
            })

        return render(request, "account/login_page.html", {
            "next": request.path
        })

    is_mobile = request.user_agent.is_mobile
    musics = Music.objects.filter(uploaded_by=request.user).prefetch_related("genres")  

    if is_mobile:
        base = "library/mobile/"
    else:
        base = "library/desktop/"

    if request.headers.get("HX-Request"):
        template = base + "library_content.html"
    else:
        template = base + "library.html"

    return render(request, template, {
        "active_page": "library",
        "musics": musics
    })
    