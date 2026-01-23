from django.db import models


class Professor(models.Model):
    choises_kafedra = (
        ("Axborot xavfsizligi", "Axborot xavfsizligi"),
        ("Axborot texnologiyalari", "Axborot texnologiyalari"),
        ("Raqamli ta'lim texnologiyalari", "Raqamli ta'lim texnologiyalari"),
        ("Dasturiy injiniring", "Dasturiy injiniring"),
        ("Gumanitar va ijtimoiy fanlar", "Gumanitar va ijtimoiy fanlar"),
        ("Kompyuter tizimlari kafedrasi", "Kompyuter tizimlari kafedrasi"),
        ("Tabiiy fanlar", "Tabiiy fanlar"),
        ("Telekommunikatsiya injiniringi", "Telekommunikatsiya injiniringi"),
        ("Tillar kafedrasi", "Tillar kafedrasi"),
    )
    
    choises_fakutet = (
        ("Kompyuter inginirinigi", "Kompyuter inginiringi"),
        ("Axborot texnologiyalari", "Axborot texnologiyalari")
    )


    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    qabul_sana = models.DateField()
    chiqish_sana = models.DateField(null=True, blank=True)

    shartnoma_raqami = models.IntegerField(unique=True)
    shartnoma_bekor_sana = models.DateField(null=True, blank=True)
    ishlagan_fakultet  = models.CharField(choices=choises_fakutet)

    ishlagan_bolimi = models.CharField(
        max_length=100,
        choices=choises_kafedra
    )

    pasport = models.CharField(
        max_length=20,
        unique=True
    )

    buyruq = models.FileField(
        upload_to="professor_buyruqlari/",
        null=True,
        blank=True
    )
    is_active = models.BooleanField(null=True, default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.ishlagan_bolimi} ({self.ishlagan_fakultet})"
