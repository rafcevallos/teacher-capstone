from django.contrib.auth.models import User
from django.db import models

"""
purpose of module: model for profile
notes: this model has a one-to-one relationship with the user model
"""

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    classroom = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    class Meta:
        db_table = "profile"

    def __str__(self):
        return str(self.user)