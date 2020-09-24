from django.db import models


class Quote(models.Model):
    author = models.CharField(default="Anonim", max_length=25, blank=False)
    quote = models.TextField(max_length=100, blank=False)


class Comment(models.Model):
    username = models.CharField(default="Anonim", max_length=30, blank=False)
    content = models.TextField(blank=False)
    date = models.DateTimeField(auto_now_add=True)
    page = models.CharField(default="comp_t", blank=False, max_length=10, choices=[('comp_t', "Computational Thinking"),
                                                                                   ('data_r', "Data Representation"),
                                                                                   ('algo', 'algorithms'),
                                                                                   ('code', 'Code')])
