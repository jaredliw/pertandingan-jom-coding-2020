from django.urls import path
from . import views


urlpatterns = [
    path('computational_thinking', views.comp_t, name='q-comp_t'),
    path('data_representation', views.data_r, name='q-data_r'),
    path('algorithms', views.algo, name='q-algo'),
    path('code', views.code, name='q-code'),
]