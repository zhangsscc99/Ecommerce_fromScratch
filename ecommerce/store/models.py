from django.db import models

# Create your models here.
class Category(models:Model):

    name = models.CharField(max_length=250, db_index=True)
    #query acceleration  
    #not gonna read the entire model 
    slug = models.SlugField(max_length=250, unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    #Category (1), Category (2) Shirt Shoes 
    def __str__(self):
        return self.name 

class Product(models.Model):
    title = models.CharField(max_length=250)

    brand = models.CharField(max_length=250, default='un-branded')

    description = models.TextField(blank=True)

    slug = models.SlugField(max_length=255)

    price = models.DecimalField(max_digits=4, decimal_places=2)

    # image = models.ImageField(upload_to='images/')



    class Meta:
        verbose_name_plural = 'products'

    #Category (1), Category (2) Shirt Shoes 
    def __str__(self):
        return self.title
