from django.db import models


class Skill(models.Model):
    name = models.CharField(default="", max_length=200)
    resources = models.CharField(default="", max_length=500)

    class Meta:
        db_table: "Skill"

    def __str__(self):
        return self.name