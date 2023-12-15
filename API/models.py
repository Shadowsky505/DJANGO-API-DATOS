from django.db import models


class Datos(models.Model):
    id = models.CharField(max_length=40,primary_key=True)
    IDSensor = models.CharField(max_length=40)
    nivelContaminacion = models.DecimalField(
        default=0.0, decimal_places=1, max_digits=3
    )
    latitud = models.DecimalField(default=0.0, decimal_places=6, max_digits=10)
    longitud = models.DecimalField(default=0.0, decimal_places=6, max_digits=10)
    fechaRegistro = models.CharField(max_length=20)
    horaPub = models.CharField(max_length=20)
    minutoPub = models.CharField(max_length=20)
    segundoPub = models.CharField(max_length=20)

    def __str__(self):
        return self.IDSensor
