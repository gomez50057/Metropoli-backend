from django.core.exceptions import ValidationError
import os

def validar_tipo_archivo(archivo):
    ext = os.path.splitext(archivo.name)[1].lower()
    tipos_validos = ['.pdf', '.png', '.jpg', '.jpeg', '.xlsx', '.csv']
    if ext not in tipos_validos:
        raise ValidationError(f'Tipo de archivo no permitido: {ext}')
