from django.urls import path
from . import views


urlpatterns = [
    path('1/', views.quiz1, name='home'),
]