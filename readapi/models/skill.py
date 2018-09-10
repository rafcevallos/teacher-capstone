from django.db import models
from .reading_level import ReadingLevel


class Skill(models.Model):
    reading_level = models.ForeignKey(ReadingLevel, null=True, on_delete=models.CASCADE)
    name = models.CharField(default="", max_length=200)

    class Meta:
        db_table = "Skill"

    def __str__(self):
        return self.name