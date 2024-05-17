from django.db import models

# Create your models here.

class Hasta(models.Model):
    id=models.AutoField(primary_key=True)
    HastaID=models.CharField(max_length=100)
    Ad = models.CharField(max_length=100)
    Soyad = models.CharField(max_length=100)
    DogumTarihi = models.DateField()
    Cinsiyet = models.CharField(max_length=10)
    TelefonNumarasi = models.CharField(max_length=15)
    Adres = models.TextField()

class Doktor(models.Model):
    id=models.AutoField(primary_key=True)
    DoktorID=models.CharField(max_length=100)
    Ad = models.CharField(max_length=100)
    Soyad = models.CharField(max_length=100)
    UzmanlikAlani = models.CharField(max_length=100)
    CalistigiHastane = models.CharField(max_length=100)

class Randevu(models.Model):
    id=models.AutoField(primary_key=True)
    RandevuTarihi = models.DateField()
    RandevuSaati = models.CharField(max_length=10)
    Hasta = models.ForeignKey(Hasta, on_delete=models.CASCADE)
    Doktor = models.ForeignKey(Doktor, on_delete=models.CASCADE)

class TibbiRapor(models.Model):
    id=models.AutoField(primary_key=True)
    RaporTarihi = models.DateField()
    RaporIcerigi = models.TextField()
    RaporImage=models.ImageField(upload_to="images",blank=True)
    Hasta = models.ForeignKey(Hasta, on_delete=models.CASCADE)
    Doktor = models.ForeignKey(Doktor, on_delete=models.CASCADE)
