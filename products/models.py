from django.db import models
import random 
import os 

def get_file_ext(filepath):
    base_name = os.path.basename(filepath)
    ext = os.path.splitext(base_name)
    return base_name, ext 

def upload_image_path(instance, filename):
    new_filename= random.randint(1,123123123)
    name , ext = get_file_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'{new_filename}/{final_filename}'

class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True)

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def get_by_id(self,id):
        return self.get_queryset().filter(id=id)

    def featured(self):
        return get_queryset().featured()


class Product(models.Model):
    title = models.CharField(max_length=150 )
    description = models.TextField(max_length=1000, blank=True , )
    price  = models.DecimalField(decimal_places=3, max_digits=10, default=0.00 )
    featured = models.BooleanField(default=True)
    image = models.ImageField(
                            upload_to= upload_image_path, 
                            blank=True,
                            default='https://images.unsplash.com/photo-1554744512-d6c603f27c54?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80'
                            )

    
    objects = ProductManager()

    def __str__(self):
        return self.title