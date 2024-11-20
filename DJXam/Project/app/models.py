from django.db import models

# Create your models here.
class author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=225)

    def __str__(self):
        return f"{self.name}"

class publisher(models.Model):
    name = models.CharField(max_length=50)
    location = models.TextField(max_length=225)

    def __str__(self):
        return f"{self.name}"
    
class book(models.Model):
    title = models.TextField(max_length=150)
    author_name = models.CharField(max_length=50)
    publisher_name = models.CharField(max_length=50)
    publication_year = models.IntegerField()

    def __str__(self):
        return f"{self.title}"
    
##

class post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.title}"
    

class category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.name}"
    

class comment(models.Model):
    content_title = models.CharField(max_length=50)
    content = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.content_title}"