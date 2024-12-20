from django.db import models
from taskcategories.models import TaskCategory
# Create your models here.



class Task(models.Model):
    taskTitle = models.CharField(max_length=50)
    taskDescription = models.TextField()
    category = models.ManyToManyField(TaskCategory)
    is_completed = models.BooleanField(default=False)
    assignDate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.taskTitle