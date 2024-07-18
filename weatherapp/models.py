from django.db import models
from django.contrib.auth.models import User


class City(models.Model):
    name = models.CharField(max_length=40)
   

    def __str__(self) -> str:
        return self.name

  

