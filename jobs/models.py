from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='jobs/images/')
    summary = models.CharField(max_length=200)
    github_page = models.URLField()
    viewer = models.URLField()
    
    def __str__(self):
        return self.title