from django.db import models
from django.contrib.auth.models import User

class Talaba(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    talaba_id = models.CharField(max_length=20, unique=True)
    guruh = models.CharField(max_length=50)
    fakultet = models.CharField(max_length=100)
    telefon = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.talaba_id}"

class BitiruMalakaviyIsh(models.Model):
    HOLAT_TANLOVI = [
        ('tayyorlanmoqda', 'Tayyorlanmoqda'),
        ('tekshiruvda', 'Tekshiruvda'),
        ('rad_etildi', 'Rad etildi'),
        ('tasdiqlandi', 'Tasdiqlandi'),
    ]
    
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE, related_name='bitiruv_ishlari')
    mavzu = models.CharField(max_length=500)
    ilmiy_rahbar = models.CharField(max_length=200)
    taqdimot_sanasi = models.DateField(null=True, blank=True)
    fayl = models.FileField(upload_to='bitiruv_ishlari/', null=True, blank=True)
    holat = models.CharField(max_length=20, choices=HOLAT_TANLOVI, default='tayyorlanmoqda')
    ball = models.IntegerField(null=True, blank=True)
    izoh = models.TextField(blank=True)
    yuklangan_sana = models.DateTimeField(auto_now_add=True)
    yangilangan_sana = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "Bitiruv Malakaviy Ish"
        verbose_name_plural = "Bitiruv Malakaviy Ishlari"
        ordering = ['-yuklangan_sana']
    
    def __str__(self):
        return f"{self.talaba.user.get_full_name()} - {self.mavzu[:50]}"

class Fayl(models.Model):
    FAYL_TURI = [
        ('ish', 'Bitiruv ishi'),
        ('taqdimot', 'Taqdimot'),
        ('ilova', 'Ilova'),
    ]
    
    bitiruv_ishi = models.ForeignKey(BitiruMalakaviyIsh, on_delete=models.CASCADE, related_name='fayllar')
    fayl = models.FileField(upload_to='bmi_fayllar/')
    fayl_turi = models.CharField(max_length=20, choices=FAYL_TURI)
    nomi = models.CharField(max_length=200)
    yuklangan_sana = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nomi} - {self.fayl_turi}"

class Baholash(models.Model):
    bitiruv_ishi = models.ForeignKey(BitiruMalakaviyIsh, on_delete=models.CASCADE, related_name='baholashlar')
    baholovchi = models.CharField(max_length=200)
    ball = models.IntegerField()
    izoh = models.TextField()
    sana = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.baholovchi} - {self.ball} ball"