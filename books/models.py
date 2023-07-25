from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=250)
    subtitle=models.CharField(max_length=250)
    author=models.CharField(max_length=100)
    isnb=models.CharField(max_length=30)

    def __str__(self):
        return self.title