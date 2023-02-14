from django.contrib import admin


from policia.models import Policia


class PoliciaAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "email", "nui")


admin.site.register(Policia, PoliciaAdmin)
