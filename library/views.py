from django.shortcuts import render

def library(request):
    if request.headers.get("HX-Request"):
        return render(request, "library/library_content.html", {
        'active_page': 'library'
        }
    )

    return render(request, "library/library.html",{
        'active_page': 'library'
    })