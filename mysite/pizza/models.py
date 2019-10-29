from django.db import models

class Topping(models.model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.Models
