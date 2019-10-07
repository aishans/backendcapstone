from django.contrib import admin

from django.contrib import admin
from .models import (Profile, School, Category, Subject, Question, Answer)

admin.site.register(Profile)
admin.site.register(School)
admin.site.register(Category)
admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Answer)
