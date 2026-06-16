from django.contrib import admin

from institucion.models import *


# Register your models here.
class MuseoAdmin(admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str)
    # de la clase
    list_display = ("nombre", "ciudad", "anio_fundacion")
    search_fields = ("nombre", "ciudad")


admin.site.register(Museo, MuseoAdmin)
admin.site.register(GuiaMuseo)
admin.site.register(Exhibicion)
