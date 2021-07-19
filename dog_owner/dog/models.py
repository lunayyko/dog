from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=254)
    age = models.BigIntegerField
    class Meta: 
        db_table = 'owners' 
    def __str__(self):
        return self.name

class Dog(models.Model):
    name = models.CharField(max_length=45)
    owner = models.ForeignKey('Owner', on_delete=models.CASCADE, default='')
    age = models.BigIntegerField
    class Meta:
        db_table='dogs'  
    def __str__(self):
        return self.name