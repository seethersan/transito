from django.contrib import admin


from policia.models import Policia

class PoliciaAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_first_name', 'get_last_name', 'get_email', 'nui', 'birth_date')

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_email(self, obj):
        return obj.user.email

admin.register(Policia, PoliciaAdmin)