from django.db import models
from django.contrib.auth.models import User, Group
from django.core.validators import MaxValueValidator, MinValueValidator 
from django.utils import timezone

gender_choices = [
    ('นาย', 'นาย'),
    ('นางสาว', 'นางสาว'),
]
type_choices = [
    ('IS', 'อาจารย์ผู้สอน'),
    ('TA', 'นักศึกษาผู้ช่วยสอน')
]
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=gender_choices)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
    student_id = models.IntegerField()
    email_ref = models.EmailField()
    group_ref = models.CharField(max_length=25)
    score = models.PositiveIntegerField(default=10, validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return str(self.user)

class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=6, choices=gender_choices)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
    type = models.CharField(max_length=2, choices=type_choices)

    def __str__(self):
        return str(self.user)

class Content_Base(models.Model):
    class Meta:
        abstract = True

    author = models.OneToOneField(Instructor, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=timezone.now)
    content = models.CharField(max_length=3000)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.subject

class Course_Content(Content_Base):
    class Meta:
        verbose_name = 'Course Content'
        verbose_name_plural = 'Course Contents'

class Assignments(Content_Base):
    due_date = models.DateTimeField()
    max_score = models.IntegerField()

class Course_Comment(Content_Base):
    class Meta:
        verbose_name = 'Course Comment'
        verbose_name_plural = 'Course Comments'

    content = models.ForeignKey(Course_Content, on_delete=models.CASCADE)


class Classwork(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assignment = models.OneToOneField(Assignments, on_delete=models.CASCADE)
    submit_date = models.DateTimeField(default=timezone.now)
    score = models.IntegerField(null=True)
    graded = models.BooleanField(default=False)

    def __str__(self):
        return str(self.user)