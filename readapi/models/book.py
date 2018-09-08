from django.db import models
from .genre import Genre


class Book(models.Model):
    title = models.CharField(default="", max_length=30)
    author = models.CharField(default="", max_length=100)
    word_count = models.IntegerField()
    unit = models.CharField(default="", max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    class Meta:
        db_table = "Book"

    def __str__(self):
        return self.title