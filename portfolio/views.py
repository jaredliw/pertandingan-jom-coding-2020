from django.shortcuts import render

kwargs = {
    "nav_styling": "background-color: #FFF;",
    "nav_text_styling": "color: #000;"
}


def home(request):
    return render(request, "portfolio/home.html", kwargs)
