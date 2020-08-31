from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Assignment(models.Model):
    title = models.CharField(max_length=50)
    story = models.TextField(max_length=5000)

    def __str__(self):
        return self.title
    
class Choice(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Question(models.Model):
    assignment = models.ForeignKey(
        Assignment, on_delete=models.CASCADE, related_name='questions', blank=True, null=True)
    question = models.CharField(max_length=200)
    choices = models.ManyToManyField(Choice)
    answer = models.ForeignKey(
        Choice, on_delete=models.CASCADE, related_name='answer', blank=True, null=True)
    order = models.SmallIntegerField()

    def __str__(self):
        return self.question
    
class GradedAssignment(models.Model):
    asnt = models.CharField(max_length=200, blank=True, null=True)
    grade = models.FloatField()
   
    def __str__(self):
        return str(self.grade)


class LogMessage(models.Model):
    message = models.CharField(max_length=300)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"