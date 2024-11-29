from django.db import models
import datetime
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text= models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
from django.db import models

class Student(models.Model):
    # Define fields for the student model
    id = models.AutoField(primary_key=True)  # Automatically increments (Primary Key)
    name = models.CharField(max_length=100)  # Name of the student
    city = models.CharField(max_length=100)  # City where the student resides
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)  # CGPA with two decimal places

    # String representation of the object
    def __str__(self):
        return self.name
    

class Teacher(models.Model):
    # Define fields for the student model
    id = models.AutoField(primary_key=True)  # Automatically increments (Primary Key)
    name = models.CharField(max_length=100)  # Name of the student
    city = models.CharField(max_length=100)  # City where the student resides
    cgpa = models.DecimalField(max_digits=4, decimal_places=2)  # CGPA with two decimal places

    # String representation of the object
    def __str__(self):
        return self.name