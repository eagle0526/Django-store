from django.db import models
from django.urls import reverse
# Create your models here.


class Employer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        ordering = ['last_name', 'first_name']
    
    def get_absolute_url(self):
        return reverse('employer-detail', args=[str(self.id)])
    
    def __str__(self):
        return f'{self.first_name}-{self.last_name}'










