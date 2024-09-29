from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Profil(models.Model):
    ism = models.CharField(max_length=255)
    yosh = models.PositiveSmallIntegerField()
    sana = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.ism


class Kurs(models.Model):
    DARAJA_CHOICES = (
        ('Yengil', 'Yengil'),
        ('O\'rta', 'O\'rta'),
        ('Yuqori', 'Yuqori'),
    )

    nom = models.CharField(max_length=255)
    daraja = models.CharField(max_length=50, choices=DARAJA_CHOICES, default='Yuqori')
    ustoz = models.CharField(max_length=255)
    narx = models.FloatField(validators=[MinValueValidator(0)])
    chegirma = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.nom


class Izoh(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    matn = models.TextField(blank=True, null=True)
    baho = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)], default=5)

    def __str__(self):
        return f"{self.profil} - {self.kurs}"


class Tanlangan(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.profil} - {self.kurs}"


class Xarid(models.Model):
    HOLAT_CHOICES = (
        ('To\'lov kutilmoqda', 'To\'lov kutilmoqda'),
        ("To'landi", "To'landi")
    )

    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    kurs = models.ForeignKey(Kurs, on_delete=models.CASCADE)
    holat = models.CharField(max_length=50, choices=HOLAT_CHOICES, default='To\'lov kutilmoqda')
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.profil} - {self.kurs}"
