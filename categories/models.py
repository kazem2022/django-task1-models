from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.title
    
class Producer(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
class Product(models.Model):
    producer = models.ForeignKey(Producer)
    category = models.ForeignKey(Category)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=50)
    photo = models.ImageField()
    is_enable = models.BooleanField(default=False)