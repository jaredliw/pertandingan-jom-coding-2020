from django.shortcuts import render


def home(request):
    kwargs = {
        "home": 1
    }
    return render(request, "home/home.html", kwargs)
