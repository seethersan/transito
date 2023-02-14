from rest_framework import serializers


from persona.models import Persona


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ("email", "first_name", "last_name")
