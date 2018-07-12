from django.db import models

maxShortTitleLength = 50

class Learning(models.Model):
    learning_text = models.TextField(max_length=3000)

    def __str__(self):
        length = len(self.learning_text)
        if length > maxShortTitleLength + 1:
            title = self.learning_text[:maxShortTitleLength] + '…'
        else:
            title = self.learning_text
        return title
