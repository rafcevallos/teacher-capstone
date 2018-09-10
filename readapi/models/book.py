from django.db import models
from .genre import Genre


# Is it possible to sort Books by UNIT?
class Book(models.Model):
    READING_LEVEL = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    )
    title = models.CharField(default="", max_length=30)
    author = models.CharField(default="", max_length=100)
    level = models.CharField(max_length = 1, default='', choices = READING_LEVEL)
    word_count = models.IntegerField()
    unit = models.CharField(default="", max_length=50)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    notes = models.TextField(default="", blank=True)

    class Meta:
        db_table = "Book"

    def __str__(self):
        return self.title
