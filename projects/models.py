from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.FilePathField(path="projects\static\img")


#To start the process of creating our database, we need to create a migration
#python manage.py makemigrations projects
#projects/migrations/0001_initial.py