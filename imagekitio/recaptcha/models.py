from django.db import models
import datetime

# Create your models here.
class IPModel(models.Model):
    ip = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return str(self.ip) +"-"+ str(self.date)

