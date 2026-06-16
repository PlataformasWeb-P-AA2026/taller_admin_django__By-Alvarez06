from django.contrib import admin

from institucion.models import *


# Register your models here.
class MuseoAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = (
        "nombre",
        "ciudad",
        "calcular_costo_total",
        "obtener_guias_lideres",
        "anio_fundacion",
    )
    search_fields = ("nombre", "ciudad")


admin.site.register(Museo, MuseoAdmin)


class GuiaMuseoAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ("nombre_completo", "anios_experiencia_guia", "idiomas_hablados")
    search_fields = ("nombre_completo", "anios_experiencia_guia", "idiomas_hablados")


admin.site.register(GuiaMuseo, GuiaMuseoAdmin)


class ExhibicionAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = (
        "titulo_exhibicion",
        "duracion_meses",
        "costo_produccion",
        "tematica",
    )
    search_fields = (
        "titulo_exhibicion",
        "duracion_meses",
        "costo_produccion",
        "tematica",
    )


admin.site.register(Exhibicion, ExhibicionAdmin)
