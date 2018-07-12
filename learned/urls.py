from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('learning/<int:id>', views.learning, name='learning'),
]
