from django.shortcuts import render

from .models import Learning

def index(request):
    learnings = Learning.objects.all()
    context = {
        'learnings': learnings
    }
    return render(request, 'learnings.html', context)

def learning(request, id):
    learning = Learning.objects.get(pk=id)
    context = {
        'learning': learning,
        'meta': learning._meta
    }
    return render(request, 'learning.html', context)