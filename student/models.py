from django.db import models

# Create your models here.

class Students(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    address = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=20)

    def __str__(self):
        return self.name