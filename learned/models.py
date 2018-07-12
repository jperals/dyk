from django.db import models

class Learning(models.Model):
    learning_text = models.TextField(max_length=3000)
