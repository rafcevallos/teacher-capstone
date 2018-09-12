from django.db import models
from .reading_level import ReadingLevel


class Skill(models.Model):
    name = models.CharField(default="", max_length=500)
    is_reader = models.BooleanField(default=True)
    reading_level = models.ForeignKey(ReadingLevel, null=True, on_delete=models.CASCADE)

    class Meta:
        db_table = "Skill"

    def __str__(self):
        return self.name