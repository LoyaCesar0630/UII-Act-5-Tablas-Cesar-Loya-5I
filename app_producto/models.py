from django.db import models

# Create your models here.

class producto(models.Model):
    marca= models.CharField(max_length=100)
    talla= models.CharField(max_length=100)
    precio= models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.marca} {self.precio}"