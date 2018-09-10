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

    book_photo = models.FileField(blank=True,upload_to='bookphotos/')
    title = models.CharField(default="", blank=True, max_length=100)
    author = models.CharField(default="", blank=True, max_length=100)
    level = models.CharField(max_length = 1, default='', blank=True, choices = READING_LEVEL)
    word_count = models.IntegerField(blank=True)
    unit = models.CharField(default="", blank=True, max_length=50)
    genre = models.ForeignKey(Genre, null=True, on_delete=models.CASCADE)
    notes = models.TextField(default="", blank=True)

    class Meta:
        db_table = "Books"

    def __str__(self):
        return self.title
