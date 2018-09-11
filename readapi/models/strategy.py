from django.db import models

# # should I add choices to this model instead of typing each property of the model?
class Strategy(models.Model):
    name = models.CharField(default="", max_length=100)

    class Meta:
        db_table = "Strategy"

    def __str__(self):
        return self.name