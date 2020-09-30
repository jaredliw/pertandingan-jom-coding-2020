from django.urls import path

from . import views

urlpatterns = [
    path('computational_thinking', views.comp_t, name='comp_t'),
    path('data_representation', views.data_r, name='data_r'),
    path('algorithms', views.algo, name='algo'),
    path('code', views.code, name='code'),
    path('base_converter', views.base_c, name='base_c')
]
