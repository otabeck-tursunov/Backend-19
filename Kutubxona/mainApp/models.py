from django.db import models

class Talaba(models.Model):
    ism = models.CharField(max_length=255)
    guruh = models.CharField(max_length=50)
    kurs = models.PositiveSmallIntegerField(default=1)
    kitob_soni = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.ism

class Muallif(models.Model):
    JINS = (
        ('Erkak', 'Erkak'),
        ('Ayol', 'Ayol'),
    )

    ism = models.CharField(max_length=255)
    jins = models.CharField(max_length=10, choices=JINS)
    t_sana = models.DateField(blank=True, null=True)
    kitob_soni = models.PositiveSmallIntegerField(blank=True, null=True)
    tirik = models.BooleanField(default=False)

    def __str__(self):
        return self.ism


class Kitob(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=20)
    sahifa = models.PositiveSmallIntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Kutubxonachi(models.Model):
    ISH_VAQTI = (
        ('1', '08:00 - 13:00'),
        ('2', '13:00 - 19:00'),
    )

    ism = models.CharField(max_length=255)
    ish_vaqti = models.CharField(max_length=40, choices=ISH_VAQTI)

    def __str__(self):
        return self.ism


class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=models.CASCADE)

    olingan_sana = models.DateTimeField(auto_now_add=True)
    qaytargan_sana = models.DateTimeField(blank=True, null=True)
    qaytardi = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.talaba} - {self.kitob} - {self.kutubxonachi} - {self.olingan_sana}"
