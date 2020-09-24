from django.shortcuts import render, redirect
from django.urls import resolve
from .models import Quote, Comment
from random import choice
from urllib import parse

kwargs = {
    "nav_styling": "background-color: #FFF;",
    "nav_text_styling": "color: #000;",
    "author": "Jayden Teh Jing Siang"
}

def preprocess(func):
    def process(request):
        quotes = Quote.objects.all()
        quote = choice(quotes)
        kwargs["quote"] = quote.quote
        kwargs["quote_author"] = quote.author

        comments = Comment.objects.all()
        kwargs["comments"] = comments

        # Get name by path, refer to .urls.py for more infomation
        path_name = resolve(request.path_info).url_name
        kwargs["page"] = path_name
        if request.method == "POST":
            data = dict(parse.parse_qsl(request.body))
            Comment(username=data[b'username'].decode(), content=data[b'comment'].decode()).save()
            # Redirect POST to GET, preventing reeated POST on reload
            return redirect(path_name)
        return func(request)
    return process

@preprocess
def comp_t(request):
    kwargs["title"] = "Teknik Pemikiran Komputasional"
    kwargs["cover_img"] = "images/1.jpg"
    kwargs["subtitile"] = "to be added..."
    return render(request, 'curriculum/comp_t.html', kwargs)

@preprocess
def data_r(request):
    kwargs["title"] = "Perwakilan Data"
    kwargs["cover_img"] = "images/2.jpg"
    kwargs["subtitile"] = "to be added..."
    return render(request, 'curriculum/data_r.html', kwargs)

@preprocess
def algo(request):
    kwargs["title"] = "Algorithma"
    kwargs["cover_img"] = "images/3.jpg"
    kwargs["subtitile"] = "to be added..."
    return render(request, 'curriculum/algo.html', kwargs)

@preprocess
def code(request):
    kwargs["title"] = "Kod Arahan"
    kwargs["cover_img"] = "images/3.jpg"
    kwargs["subtitile"] = "to be added..."
    return render(request, 'curriculum/code.html', kwargs)
