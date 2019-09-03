import datetime
from django.shortcuts import render
from django.utils import timezone

from .models import Learning


def index(request):
    learnings = Learning.objects.order_by('-created_date')
    learnings_by_day = {}
    today = timezone.now().date()
    for learning in learnings:
        if learning.status == 'published' or request.user.has_perm('learned.change_learning'):
            date = learning.created_date.date()
            days_ago = abs((today - date).days)
            if days_ago not in learnings_by_day:
                learnings_by_day[days_ago] = {
                    'date': date,
                    'days_ago': days_ago,
                    'learnings': []
                }
            learnings_by_day[days_ago]['learnings'].append(learning)
    context = {
        'learnings': learnings_by_day,
        'meta': Learning._meta
    }
    return render(request, 'learnings.html', context)

def learning(request, id):
    learning = Learning.objects.get(pk=id)
    context = {
        'learning': learning,
        'meta': learning._meta
    }
    return render(request, 'learning.html', context)