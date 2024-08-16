from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null = True, 
        blank = True,
        )


    def __str__(self):
        return self.name

#teste 1 (Fellipe):
#Alterado no github
