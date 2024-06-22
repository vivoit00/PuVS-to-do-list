from django.db import models

class Todo(models.Model):
    todo = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.todo 