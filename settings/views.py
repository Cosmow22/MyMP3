from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def settings(request):
    if not request.user.is_authenticated:
        if request.headers.get("HX-Request"):
            return render(request, "account/login.html", {
                "next": request.path
            })

        return render(request, "settings/settings_login.html", {
            "next": request.path
        })

    if request.headers.get("HX-Request"):
        return render(request, "settings/settings_content.html")

    return render(request, "settings/settings.html")

@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        return redirect("home")
    return redirect("home")