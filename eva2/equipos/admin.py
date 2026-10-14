from django.contrib import admin

class EquipoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'marca', 'modelo', 'estado', 'fecha_adquisicion')
    search_fields = ('nombre', 'marca', 'modelo')