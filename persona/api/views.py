from rest_framework import viewsets
from rest_framework import permissions


from persona.models import Persona
from persona.api.serializers import PersonaSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [permissions.IsAuthenticated]
