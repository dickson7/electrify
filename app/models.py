from django.db import models
from django.contrib .auth.models import User
# Create your models here.


class Equipment(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    equipment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=30)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Maintenance(models.Model):
    maintenance_id = models.AutoField(primary_key=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return f"Maintenance ID: {self.maintenance_id}"

class Readings(models.Model):
    reading_id = models.AutoField(primary_key=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.FloatField()

    def __str__(self):
        return f"Reading ID: {self.reading_id}"