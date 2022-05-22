from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Task(models.Model):
    title = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userTasks")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="categoryTasks")
    date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title}"
    
    def is_valid_task(self):
        return len(self.title) < 65
