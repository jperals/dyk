from django.db import models

maxShortTitleLength = 50


class Learning(models.Model):
    learning_title = models.CharField(
        blank=True,
        max_length=3000
    )
    learning_text = models.TextField(max_length=3000)

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
