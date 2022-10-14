from django.urls import path
from simple import views

urlpatterns = [
    path('', views.index, name='index'),
]
