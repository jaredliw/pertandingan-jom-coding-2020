from django.shortcuts import render
from .models import Question


kwargs = {
    "nav_styling": "background-color: #FFF;",
    "nav_text_styling": "color: #000;"
}

def quiz1(request):
    kwargs["quiz_name"] = "Hello"
    kwargs["page_now"] = "1"
    kwargs["page_total"] = ""
    return render(request, 'quiz/base.html', kwargs)

# def data_r(request):
#     kwargs["title"] = "Perwakilan Data"
#     kwargs["cover_img"] = "images/2.jpg"
#     kwargs["subtitile"] = "to be added..."
#     return render(request, 'curriculum/data_r.html', kwargs)
#
# def algo(request):
#     kwargs["title"] = "Algorithma"
#     kwargs["cover_img"] = "images/3.jpg"
#     kwargs["subtitile"] = "to be added..."
#     return render(request, 'curriculum/algo.html', kwargs)
#
# def code(request):
#     kwargs["title"] = "Kod Arahan"
#     kwargs["cover_img"] = "images/3.jpg"
#     kwargs["subtitile"] = "to be added..."
#     return render(request, 'curriculum/code.html', kwargs)
