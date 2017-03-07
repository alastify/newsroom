from django.contrib import admin
from .models import Zpravy


class ZpravyAdmin(admin.ModelAdmin):
    list_display = ( 'titulek', 'datum')


admin.site.register(Zpravy, ZpravyAdmin)
