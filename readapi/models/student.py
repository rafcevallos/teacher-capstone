from django.contrib.auth.models import User
from django.db import models
from multiselectfield import MultiSelectField


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
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
    )

    SKILLS = (
        ('Decoding', 'Decoding'),
        ('Comprehension', 'Comrephension'),
        ('Fluency', 'Fluency'),
        ('Expression', 'Expression'),
        ('Picture Clues', 'Picture Clues'),
        ('Stretch It', 'Stretch It'),
        ('Chunking', 'Chunking'),
        ('Get Mouth Ready', 'Get Mouth Ready'),
        ('Go Back and Reread', 'Go Back and Reread'),
        ('Does It Make Sense?', 'Does It Make Sense?'),
        ('Does It Sound Right?', 'Does It Sound Right?'),
        ('Self-Corrects', 'Self-Corrects'),
    )

    teacher = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(default="", blank=True, max_length=30)
    last_name = models.CharField(default="",  blank=True, max_length=30)
    student_photo = models.FileField(blank=True, upload_to='studentphotos/')
    notes = models.TextField(default="", blank=True)
    reading_level = models.CharField(default="", blank=True,max_length = 1,  choices = READING_LEVEL)
    skills = MultiSelectField(default='', blank=True, choices = SKILLS)

    class Meta:
        db_table = "Student"

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
