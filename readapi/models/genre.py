from django.db import models


class Genre(models.Model):
    name = models.CharField(default="", max_length=100)

    class Meta:
        db_table = "Genre"

    def __str__(self):
        return self.name