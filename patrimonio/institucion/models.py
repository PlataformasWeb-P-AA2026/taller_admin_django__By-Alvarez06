from django.db import models

# Create your models here.


class Museo(models.Model):
    nombre = models.CharField(
        "Nombre del museo", max_length=100, unique=True, null=False, blank=False
    )
    ciudad = models.CharField(max_length=100)
    anio_fundacion = models.IntegerField("Año de fundación")

    def calcular_costo_total(self):
        """Calcula el costo sumando el resultado del método de cada guía relacionado"""
        total = 0
        for guia in self.losguias.all():
            total += guia.calcular_costo_exhibiciones()
        return total

    def obtener_guias_lideres(self):
        """Obtiene los nombres de los guías con mayor experiencia iterando sobre sus relaciones"""
        guias = self.losguias.all()
        if not guias:
            return "Sin guías asignados"

        # Encontramos la máxima experiencia utilizando lógica de Python
        max_experiencia = max(
            guias, key=lambda g: g.anios_experiencia_guia
        ).anios_experiencia_guia

        # Filtramos y concatenamos los nombres de los guías que coincidan
        guias_lideres = [
            g.nombre_completo
            for g in guias
            if g.anios_experiencia_guia == max_experiencia
        ]
        return ", ".join(guias_lideres)

    def __str__(self):
        return f"Museo: {self.nombre} - Ciudad: {self.ciudad} - Costo total exhibiciones {str(self.calcular_costo_total())} - Guía(s) Lideres {self.obtener_guias_lideres()} - Fundación: {self.anio_fundacion}"


class GuiaMuseo(models.Model):
    """ """

    nombre_completo = models.CharField("Nombre completo del guía", max_length=150)
    anios_experiencia_guia = models.IntegerField("Años de experiencia")
    idiomas_hablados = models.CharField("Idiomas hablados", max_length=150)

    # Relación: un guía de museo trabaja en un museo
    museo = models.ForeignKey(Museo, related_name="losguias", on_delete=models.CASCADE)

    def calcular_costo_exhibiciones(self):
        """Calcula el costo sumando el resultado del método de cada exhibición relacionada"""
        total = 0
        for exhibicion in self.lasexhibiciones.all():
            total += exhibicion.obtener_costo()
        return total

    def obtener_anios_experiencia(self):
        return self.anios_experiencia_guia or 0

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

    def obtener_costo(self):
        """Retorna el costo individual de la exhibición"""
        return self.costo_produccion or 0.0

    def __str__(self):
        return f"Exhibición: {self.titulo_exhibicion} - Temática: {self.tematica} - Duración: {self.duracion_meses} meses"
