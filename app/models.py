from django.db import models
from django.contrib.auth.models import User

SCHOOL_CHOICES = (
    ('---','__'),
    ('Elementary','ELEMENTARY'),
    ('MiddleSchool','MIDDLESCHOOL'),
    ('HighSchool','HIGHSCHOOL'),
)
CATEGORY_CHOICES = (
     ('---','__'),
   ('English','ENGLISH'),
   ('Math','MATH'),
   ('Arabic','ARABIC'),)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)
    courses_taken = models.CharField(max_length=120)
    points = models.IntegerField()

    def __str__(self):
        return str(self.user)

class School(models.Model):
    school_name = models.CharField(max_length=33,choices=SCHOOL_CHOICES,default='---')
    image = models.ImageField(blank=True, null=True)

class Category(models.Model):

    classification = models.ForeignKey(School,on_delete=models.CASCADE)
    category = models.CharField(max_length=33,choices=CATEGORY_CHOICES,default='---')
    image = models.ImageField(blank=True, null=True)









