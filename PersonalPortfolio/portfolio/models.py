from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    year = models.DateField()

    def __str__(self):
        return self.title
