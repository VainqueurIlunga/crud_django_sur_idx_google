from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    price= models.DecimalField(max_digits=10, decimal_places=3)
    description= models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='product-images/', blank=True, null=True)