from django.db import models
from .skill import Skill


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
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)