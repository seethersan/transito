from datetime import datetime
from rest_framework import serializers


from vehiculo.models import Vehiculo, Infraccion

class VehiculoSerializer(serializers.Serializer):
    class Meta:
        model = Vehiculo
        fields = '__all__'


class InfraccionCreateSerializer(serializers.Serializer):
    placa_patente = serializers.CharField(max_length=12)
    timestamp = serializers.DateTimeField()
    comentarios = serializers.CharField(max_length=200)

    class Meta:
        model = Infraccion
        fields = ('placa_patente', 'timestamp', 'comentarios')

    def validate(self, data):
        try:
            Vehiculo.objects.get(placa=data['placa'])
        except Vehiculo.DoesNotExist:
            raise serializers.ValidationError("El vehiculo no existe")
        
        if data["timestamp"] > datetime.now():
            raise serializers.ValidationError("La fecha no puede ser mayor a la actual")
        
        return data


class InfraccionSerializer(serializers.Serializer):
    vehiculo = VehiculoSerializer()
    timestamp = serializers.DateTimeField()
    lugar = serializers.CharField(max_length=50)
    comentarios = serializers.CharField(max_length=200)
    policia = serializers.CharField(max_length=50)

    class Meta:
        model = Infraccion
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['vehiculo'] = VehiculoSerializer(instance.vehiculo).data
        data['policia'] = instance.policia.user.first_name + ' ' + instance.policia.user.last_name
        return data