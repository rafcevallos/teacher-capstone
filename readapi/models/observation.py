from django.db import models


class Observation(models.Model):
    name = models.CharField(default="", max_length=100)

    class Meta:
        db_table = "Observation"

    def __str__(self):
        return self.name
