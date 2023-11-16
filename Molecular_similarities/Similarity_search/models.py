from django.db import models

# Create your models here.
class Compound(models.Model):
    IUPAC = models.CharField(max_length=1000, unique = True)
    Description = models.CharField(max_length=10000, unique =True)
    SMILES = models.CharField(max_length=1000, unique = True)
    Name = models.CharField(max_length=1000, unique= True)

    def __str__(self):
        return str(self.Name)