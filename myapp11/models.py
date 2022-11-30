from django.db import models

# Create your models here.
class StudentTable(models.Model):
    name=models.CharField(max_length=20)
    Department=models.CharField(max_length=50)
    Email=models.EmailField(max_length=30)
    MObile=models.IntegerField()
    Address=models.CharField(max_length=50)

    def __str__(self):
        return self.name