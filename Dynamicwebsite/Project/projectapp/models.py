from django.db import models


class Place(models.Model):  # Use 'Model' instead of 'model'
    objects = None
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name


class my_team(models.Model):  # Use 'Model' instead of 'model'
    objects = None
    name = models.CharField(max_length=250)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()

    def __str__(self):
        return self.name
