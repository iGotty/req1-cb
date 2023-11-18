from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Cita(models.Model):
    hora = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(24)])  # Hour of the cita (1-24)
    lugar = models.CharField(max_length=200)  # Location of the cita

    def __str__(self):
        return f'Cita at {self.hora}:00 in {self.lugar}'