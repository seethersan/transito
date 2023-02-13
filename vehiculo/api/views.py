from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


from vehiculo.models import Vehiculo, Infraccion
from vehiculo.api.serializers import VehiculoSerializer, InfraccionSerializer, InfraccionCreateSerializer
from policia.models import Policia
from persona.models import Persona


class VehiculoViewSet(viewsets.ModelViewSet):
    queryset = Vehiculo.objects.all()
    serializer_class = VehiculoSerializer
    permission_classes = [permissions.IsAuthenticated]


class InfraccionViewSet(viewsets.ModelViewSet):
    queryset = Infraccion.objects.all()
    serializer_class = InfraccionSerializer

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = []
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = InfraccionCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            wehiculo = Vehiculo.objects.get(placa=serializer.validated_data['placa_patente'])
            policia = Policia.objects.get(user=request.user)
            infraccion = Infraccion.objects.create(vehiculo=wehiculo, timestamp=serializer.validated_data['timestamp'], comentarios=serializer.validated_data['comentarios'], policia=policia)
            serializer = self.serializer_class(infraccion)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def list(self, request, *args, **kwargs):
        email = request.GET.get('email')
        persona = get_object_or_404(Persona, user__email=email)
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset.filter(vehiculo__propietario=persona), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)