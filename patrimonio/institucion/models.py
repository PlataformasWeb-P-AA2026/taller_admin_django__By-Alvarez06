from django.db import models

# Create your models here.


class Museo(models.Model):
    nombre = models.CharField(
        "Nombre del museo", max_length=100, unique=True, null=False, blank=False
    )
    ciudad = models.CharField(max_length=100)
    anio_fundacion = models.IntegerField("Año de fundación")

    def __str__(self):
        return f"Museo: {self.nombre} - Ciudad: {self.ciudad} - Fundación: {self.anio_fundacion}"


class GuiaMuseo(models.Model):
    """ """

    nombre_completo = models.CharField("Nombre completo del guía", max_length=150)
    anios_experiencia_guia = models.IntegerField("Años de experiencia")
    idiomas_hablados = models.CharField("Idiomas hablados", max_length=150)

    # Relación: un guía de museo trabaja en un museo
    museo = models.ForeignKey(Museo, related_name="losguias", on_delete=models.CASCADE)

    def __str__(self):
        return f"Guía: {self.nombre_completo} - Experiencia: {self.anios_experiencia_guia} años - Idiomas: {self.idiomas_hablados}"


class Exhibicion(models.Model):
    """ """

    titulo_exhibicion = models.CharField("Título de la exhibición", max_length=150)
    duracion_meses = models.IntegerField("Duración en meses")
    costo_produccion = models.DecimalField(
        "Costo de producción", max_digits=10, decimal_places=2
    )
    tematica = models.CharField("Temática principal", max_length=100)

    # Relación: una exhibición es asistida por un guía de museo
    guia = models.ForeignKey(
        GuiaMuseo, related_name="lasexhibiciones", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Exhibición: {self.titulo_exhibicion} - Temática: {self.tematica} - Duración: {self.duracion_meses} meses"
