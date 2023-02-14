from django.contrib import admin


from persona.models import Persona


class PersonaAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name")


admin.site.register(Persona, PersonaAdmin)
