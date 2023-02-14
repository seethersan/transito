from django.contrib import admin


from vehiculo.models import Vehiculo, Infraccion


class VehiculoAdmin(admin.ModelAdmin):
    list_display = ("placa", "marca", "modelo", "color", "tipo", "get_propietario")

    def get_propietario(self, obj):
        return obj.propietario.first_name + " " + obj.propietario.last_name


class InfraccionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "vehiculo",
        "timestamp",
        "lugar",
        "comentarios",
        "get_policia",
    )

    def get_policia(self, obj):
        return obj.policia.first_name + " " + obj.policia.last_name


admin.site.register(Vehiculo, VehiculoAdmin)
admin.site.register(Infraccion, InfraccionAdmin)
