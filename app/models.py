from django.db import models
from django.contrib.auth.models import User

SCHOOL_CHOICES = (
    ('---', '__'),
    ('المرحله الأبتدائيه', 'المرحله الأبتدائيه'),
    ('المرحله المتوسطه', 'المرحله المتوسطه'),
    ('المرحله الثانويه', 'المرحله الثانويه'),
)
CATEGORY_CHOICES = (
    ('---', '__'),
    ('انجليزي', 'انجليزي'),
    ('الرياضيات', 'الرياضيات'),
    ('العربيه', 'اللغه العربيه'),)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    courses_taken = models.CharField(max_length=120, default="")
    points = models.IntegerField(default=0)
    is_teacher= models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)


class School(models.Model):
    school_name = models.CharField(
        max_length=33, choices=SCHOOL_CHOICES, default='---')
    image = models.ImageField(blank=True, null=True)


class Category(models.Model):
    classification = models.ForeignKey(School, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=33, choices=CATEGORY_CHOICES, default='---')
    image = models.ImageField(blank=True, null=True)


class Subject(models.Model):
    category_subject = models.ForeignKey(Category, on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=120)
    teacher_name = models.CharField(max_length=120)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)


class Question(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = models.TextField()


class Answer(models.Model):
    is_correct = models.BooleanField(default=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=120)
