from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("call_simple_function", views.call_simple_function)
]
