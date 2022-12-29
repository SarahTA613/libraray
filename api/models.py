from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Books(models.Model):
    image = models.ImageField(null=False, blank=False)
    category = models.ForeignKey(Category, on_delete= models.CASCADE)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null= True)
    author = models.TextField(blank=True, null= True)
    publisher = models.CharField(max_length=250)
    
    

    

    def __str__(self):
        return self.title