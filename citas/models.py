from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Appointment(models.Model):
    hora = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(24)])  # Hour of the appointment (1-24)
    lugar = models.CharField(max_length=200)  # Location of the appointment

    def __str__(self):
        return f'Appointment at {self.hora}:00 in {self.lugar}'