from django.shortcuts import render

def library(request):
    is_mobile = request.user_agent.is_mobile

    if is_mobile:
        base = "library/mobile/"
    else:
        base = "library/desktop/"

    if request.headers.get("HX-Request"):
        template = base + "library_content.html"
    else:
        template = base + "library.html"

    return render(request, template, {
        'active_page': 'library'
    })