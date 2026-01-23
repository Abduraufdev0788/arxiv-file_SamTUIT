from django.db import models

class Registration(models.Model):
    ROLE = (
        ("Admin", "Admin"),
        ("Custom", "Custom")
    )
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    role = models.CharField(choices=ROLE, null=True, default="Custom")

    def __str__(self):
        return f"{self.id}. {self.name} ---- {self.role}"
