from django.db import models


class ReadingLevel(models.Model):
    READING_LEVEL = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    )
    level = models.CharField(max_length = 1, default='', choices = READING_LEVEL)

    class Meta:
        db_table = "Reading_Level"

    def __str__(self):
        return self.level