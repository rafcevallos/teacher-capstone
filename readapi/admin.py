from django.contrib import admin
from .models import Student, Book, Profile, Skill, Genre, Strategy, ReadingLevel, ConferenceLog, Observation
# Register your models here.
admin.site.register(Student)
admin.site.register(Book)
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Genre)
admin.site.register(Strategy)
admin.site.register(ReadingLevel)
admin.site.register(ConferenceLog)
admin.site.register(Observation)