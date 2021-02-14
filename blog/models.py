from django.db import models

class BlogPost(models.Model):
    
    title = models.CharField(max_length=100)
    date = models.DateField()
    blogPost = models.TextField(blank = True)
    
    def __str__(self):
        return self.title
