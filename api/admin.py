from django.contrib import admin
from .models import *

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    fields = ['group_ref','student_id', ('gender', 'name', 'surname')]
    list_filter = ['group_ref', 'gender']
    
@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    fields = [('gender','name','surname'), 'type']

@admin.register(Course_Content)
class ContentAdmin(admin.ModelAdmin):
    fields = ['pub_date']
@admin.register(Course_Comment)
class CommentAdmin(ContentAdmin):
    pass

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    fields= ['pub_date', 'due_date']

@admin.register(Classwork)
class ClassworkAdmin(admin.ModelAdmin):
    fields= ['submit_date', 'score']

# Register your models here.
