from django.db import models

class BmiTalaba(models.Model):
    choises = (
        ("Kompyuter_inginiringi", "Kompyuter_inginiringi"),
        ("Axborot_texnologiyalar", "Axborot_texnologiyalar")
        )
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    faculty = models.CharField(choices=choises)
    group_name = models.CharField(max_length=64)
    theme_name = models.TextField()
    years = models.CharField(max_length=32)
    total_ball = models.FloatField()
    files = models.FileField(upload_to='student_files/')

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.theme_name}  - {self.years}"
