from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Reys(models.Model):
    reys_raqami = models.CharField(max_length=100)
    reys_nomi = models.CharField(max_length=100)
    qaysi_shaxardan = models.CharField(max_length=100)
    qaysi_shaharga = models.CharField(max_length=100)
    uchish_sanasi = models.DateField()
    uchish_vaqti = models.TimeField()


    def __str__(self) -> str:
        return f'{self.reys_raqami} {self.reys_nomi}'
    
class Yolovchi(models.Model):
    ismi = models.CharField(max_length=100)
    familiyasi = models.CharField(max_length=100)
    otasi_ismi = models.CharField(max_length=100)
    email = models.EmailField()
    telefon = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.familiyasi

class Buyurtma(models.Model):
    reys = ForeignKey(Reys, on_delete=models.CASCADE)
    yolovchi = ForeignKey(Yolovchi, on_delete=models.CASCADE)