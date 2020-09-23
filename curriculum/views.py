from django.shortcuts import render
from .models import Quote
from random import choice


quotes = Quote.objects.all()
quote = choice(quotes)
kwargs = {
    "nav_styling": "background-color: #FFF;",
    "nav_text_styling": "color: #000;",
    "author": "Jayden Teh Jing Siang",
    "quote": quote.quote,
    "quote_author": quote.author
}

def comp_t(request):
    kwargs["title"] = "Teknik Pemikiran Komputasional"
    kwargs["cover_img"] = "images/1.jpg"
    kwargs["subtitile"] = "to be added..."
    return render(request, 'curriculum/comp_t.html', kwargs)

def data_r(request):
    kwargs["title"] = "Perwakilan Data"
    kwargs["cover_img"] = "images/2.jpg"
    kwargs["subtitile"] = "to be added..."
    return render(request, 'curriculum/data_r.html', kwargs)

def algo(request):
    kwargs["title"] = "Algorithma"
    kwargs["cover_img"] = "images/3.jpg"
    kwargs["subtitile"] = "to be added..."
    return render(request, 'curriculum/algo.html', kwargs)

def code(request):
    kwargs["title"] = "Kod Arahan"
    kwargs["cover_img"] = "images/3.jpg"
    kwargs["subtitile"] = "to be added..."
    return render(request, 'curriculum/code.html', kwargs)
