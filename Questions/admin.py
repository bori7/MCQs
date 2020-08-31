from django.contrib import admin

from .models import LogMessage, Assignment, Choice, Question, GradedAssignment


# Register your models here.
admin.site.register(LogMessage)
admin.site.register(Assignment)
admin.site.register(Choice)
admin.site.register(Question)
admin.site.register(GradedAssignment)