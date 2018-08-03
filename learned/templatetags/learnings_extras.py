from django import template
from django.utils import timezone
import datetime

register = template.Library()


# Filter for nice dates
# Expects an object with attributes `days_ago` and `date`
# Partly taken from:
# https://www.djangosnippets.org/snippets/116/
def days_since(data):
    """Returns number of days between today and value."""
    days_ago = data['days_ago']
    if days_ago == 0:
        return 'today'
    elif days_ago == 1:
        return 'yesterday'
    elif days_ago < 8:
        return '%s days ago' % days_ago
    else:
        # Return formatted date.
        return data['date']


register.filter('days_since', days_since)
