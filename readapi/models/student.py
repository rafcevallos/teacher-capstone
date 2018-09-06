from django.contrib.auth.models import User
from django.db import models


"""
Student Model
Inclues the following:
    -first_name is a string defaulted to ""
    -last_name is a string defaulted to ""
    -student_photo is an image field for uploading student photos
    -notes is a string text field defaulted to ""
    -

"""

class Student(models.Model):
    READING_LEVEL = (
        ('A'),
        ('B'),
        ('C'),
        ('D'),
        ('E'),
        ('F'),
    )
    first_name = models.CharField(default="", max_length=30)
    last_name = models.CharField(default="", max_length=30)
    student_photo = models.FileField(upload_to='studentphotos/')
    notes = models.TextField(default="")
    # skills =
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = "Student"

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
