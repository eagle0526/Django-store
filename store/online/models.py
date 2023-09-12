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


class Store(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    employer = models.ForeignKey(Employer, on_delete=models.SET_NULL, null=True)

    class Meta:        
        permissions = (("can_mark_store", "Set store as noticed"),)    

    def get_absolute_url(self):
        return reverse('store-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    store = models.ManyToManyField(Store)

    def display_store(self):        
        return ', '.join(store.title for store in self.store.all()[:3])    

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])

    def __str__(self):
        return self.title





