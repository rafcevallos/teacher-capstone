from django.db import models


class Observation(models.Model):
    decoding = models.BooleanField(default=False)
    comprehension = models.BooleanField(default=False)
    fluency = models.BooleanField(default=False)
    expression = models.BooleanField(default=False)

    class Meta:
        db_table = "Observation"

    def __str__(self):
        return "(%s, %s, %s, %s)" % (self.decoding, self.comprehension, self.fluency, self.expression)