from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone

maxShortTitleLength = 50


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Learning(models.Model):
    learning_title = models.CharField(
        blank=True,
        max_length=3000
    )
    learning_text = models.TextField(max_length=3000)

    created_date = models.DateTimeField(blank=True)
    modified_date = models.DateTimeField(editable=False)

    tags = models.ManyToManyField(Tag)

    def __str__(self):
        # If the learning has a title, use it as excerpt in lists.
        # Otherwise, use a fragment from the content instead.
        # In any case, shorten to a maximum length.
        title = self.learning_title
        length = len(title)
        if length is 0:
            title = self.learning_text
            length = len(title)
        if length > maxShortTitleLength + 1:
            title = title[:maxShortTitleLength] + '…'
        return title


# The fields created_date and modified_date are automatically created/modified but are still editable.
# Approach mostly based on:
# https://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add#1737078
# But using pre_save signal instead of overriding the save method, like here:
# https://www.codingforentrepreneurs.com/blog/post-save-vs-pre-save-vs-override-save-method/

def add_dates(sender, instance, *args, **kwargs):
    # On save, update timestamps
    if not instance.id:
        instance.created_date = timezone.now()
    instance.modified_date = timezone.now()


pre_save.connect(add_dates, sender=Learning)
