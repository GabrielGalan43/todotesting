from django.db import models
from django.contrib.auth.models import User


class TaskList(models.Model):
    task = models.CharField(max_length=300)
    done = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.task
