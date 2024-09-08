from django.db import models


class Book(models.Model):

    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)



