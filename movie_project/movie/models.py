from django.db import models

class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    birth_date = models.DateField()
    movie = ManyToManyField('Movie')
    class Meta:
        db_table='actors'
    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = IntegerField
    class Meta:
        db_table='movies'
    def __str__(self):
        return self.name