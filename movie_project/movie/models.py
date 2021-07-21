from django.db import models
class Actor(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    birth_date = models.DateField()
    movie = models.ManyToManyField('Movie')
    class Meta:
        db_table='actors'
    def __str__(self):
        return self.first_name + self.last_name

class Movie(models.Model):
    title = models.CharField(max_length=45)
    release_date = models.DateField()
    running_time = models.IntegerField()
    class Meta:
        db_table='movies'
    def __str__(self):
        return self.title