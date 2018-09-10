# This needs to be sorted by date on the Student Detail view - newest entires will be FIRST
from django.db import models
from readapi.models import Student, Book, Strategy, Observation, ReadingLevel


class ConferenceLog(models.Model):
    date = models.DateField(blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    observation = models.ForeignKey(Observation, on_delete=models.CASCADE)
    reading_level = models.ForeignKey(ReadingLevel, on_delete=models.CASCADE)
    comments = models.TextField(default="", blank=True)

    class Meta:
        db_table = "Conference_Log"

    def __str__(self):
        return self.date