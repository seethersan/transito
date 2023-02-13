from django.contrib import admin


from vehiculo.models import Vehiculo, Infraccion

class VehiculoAdmin(admin.ModelAdmin):
    list_display = ('placa', 'marca', 'modelo', 'color', 'tipo', 'get_propietario')

    def get_propietario(self, obj):
        return obj.propietario.user.first_name + ' ' + obj.propietario.user.last_name


class InfraccionAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'timestamp', 'lugar', 'comentarios', 'get_policia')

    def get_policia(self, obj):
        return obj.policia.user.first_name + ' ' + obj.policia.user.last_name

admin.register(Vehiculo, VehiculoAdmin)
admin.register(Infraccion, InfraccionAdmin)