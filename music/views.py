from django.shortcuts import render


def add_music(request): 
    if request.headers.get("HX-Request"):
        return render(request, "music/desktop/add_music_content.html")
    return render(request, "music/desktop/add_music.html")