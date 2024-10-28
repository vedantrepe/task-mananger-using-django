from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)
    description = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    deadline = models.DateTimeField(null=True, blank=True)  # Ensure this field is here
    start_time = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title
