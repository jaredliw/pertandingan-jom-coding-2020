from django.shortcuts import render

def curriculum(request):
    kwargs = {
        "nav_styling": "background-color: #FFF;",
        "nav_text_styling": "color: #000;"
    }
    return render(request, 'curriculum/curriculum.html', kwargs)
