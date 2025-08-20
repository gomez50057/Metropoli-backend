from django.contrib import admin
from .models import UploadEntry, UploadFile

class UploadFileInline(admin.TabularInline):
    model = UploadFile
    extra = 0
    readonly_fields = ['archivo', 'tipo_archivo']

@admin.register(UploadEntry)
class UploadEntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'nombre_contacto', 'numero_contacto', 'extension', 'fecha_creacion']
    search_fields = ['nombre', 'nombre_contacto', 'numero_contacto']
    list_filter = ['fecha_creacion']
    readonly_fields = ['fecha_creacion']
    inlines = [UploadFileInline]
