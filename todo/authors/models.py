from django.db import models

# Create your models here.

class Authors(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()

    def __str__(self):
        return self.first_name

class Biography(models.Model):
    text = models.TextField()
    author = models.OneToOneField(Authors, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author.first_name} {self.author.last_name}'

class Book(models.Model):
    name = models.CharField(max_length=64)
    author = models.ManyToManyField(Authors)

    def __str__(self):
        return self.name