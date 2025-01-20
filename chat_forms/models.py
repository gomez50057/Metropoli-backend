from django.db import models

class ChatForm(models.Model):
    name = models.CharField(
        max_length=100, 
        verbose_name="Nombre del Proyecto", 
        help_text="Nombre del proyecto (máximo 100 caracteres)"
    )
    description = models.TextField(
        max_length=500, 
        verbose_name="Descripción", 
        help_text="Descripción del proyecto (máximo 500 caracteres)"
    )
    municipalities = models.JSONField(
        verbose_name="Municipios", 
        help_text="Lista de municipios seleccionados"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última actualización")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Formulario del Chat"
        verbose_name_plural = "Formularios del Chat"
