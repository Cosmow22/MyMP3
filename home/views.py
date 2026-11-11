from django.shortcuts import render

def home(request):
    is_mobile = request.user_agent.is_mobile

    if is_mobile:
        base = "home/mobile/"
    else:
        base = "home/desktop/"

    if request.headers.get("HX-Request"):
        template = base + "home_content.html"
    else:
        template = base + "home.html"

    return render(request, template, {
        'active_page': 'home'
    })
