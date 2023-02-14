from django.utils import timezone
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


from vehiculo.models import Vehiculo, Infraccion
from persona.models import Persona


class VehiculoSerializer(serializers.Serializer):
    placa = serializers.CharField(
        max_length=10,
        required=True,
        validators=[UniqueValidator(queryset=Vehiculo.objects.all())],
    )
    marca = serializers.CharField(max_length=20, required=True)
    modelo = serializers.CharField(max_length=20, required=True)
    color = serializers.CharField(max_length=20, required=True)
    tipo = serializers.CharField(max_length=20, required=True)
    propietario = serializers.CharField(
        max_length=50, required=True, source="propietario.email"
    )

    class Meta:
        model = Vehiculo
        fields = ("placa", "marca", "modelo", "color", "tipo", "propietario")

    def create(self, validated_data):
        try:
            propietario = Persona.objects.get(
                email=validated_data["propietario"]["email"]
            )
        except Persona.DoesNotExist:
            raise serializers.ValidationError("El propietario no existe")

        validated_data["propietario"] = propietario
        return Vehiculo.objects.create(**validated_data)


class InfraccionCreateSerializer(serializers.Serializer):
    placa_patente = serializers.CharField(max_length=12)
    lugar = serializers.CharField(max_length=50)
    timestamp = serializers.DateTimeField()
    comentarios = serializers.CharField(max_length=200)

    class Meta:
        model = Infraccion
        fields = ("placa_patente", "timestamp", "lugar", "comentarios")

    def validate(self, data):
        try:
            Vehiculo.objects.get(placa=data["placa_patente"])
        except Vehiculo.DoesNotExist:
            raise serializers.ValidationError("El vehiculo no existe")

        if data["timestamp"] > timezone.now():
            raise serializers.ValidationError("La fecha no puede ser mayor a la actual")

        infraciones = Infraccion.objects.filter(
            vehiculo__placa=data["placa_patente"],
            timestamp=data["timestamp"],
            lugar=data["lugar"],
            comentarios=data["comentarios"],
        )
        if infraciones:
            raise serializers.ValidationError("La infraccion ya existe")

        return data


class InfraccionSerializer(serializers.Serializer):
    vehiculo = VehiculoSerializer()
    timestamp = serializers.DateTimeField()
    lugar = serializers.CharField(max_length=50)
    comentarios = serializers.CharField(max_length=200)
    policia = serializers.CharField(max_length=50)

    class Meta:
        model = Infraccion
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["vehiculo"] = VehiculoSerializer(instance.vehiculo).data
        data["policia"] = instance.policia.first_name + " " + instance.policia.last_name
        return data
