from django.db import models
from django.core.exceptions import ValidationError




# Create your models here.

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def clean(self):
        if not self.title:
            raise ValidationError("Title is required, please provide a short title for the notice.")
        if not self.content:
            raise ValidationError("Content is required, please provide the details of the notice.")
        
    