from django.db import models

class UploadEntry(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    nombre_contacto = models.CharField(max_length=255)
    numero_contacto = models.CharField(max_length=15)
    extension = models.CharField(max_length=10, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


def upload_to(instance, filename):
    return f"uploads/{instance.entry.id}/{filename}"

class UploadFile(models.Model):
    entry = models.ForeignKey(UploadEntry, related_name='archivos', on_delete=models.CASCADE)
    archivo = models.FileField(upload_to=upload_to)
    tipo_archivo = models.CharField(max_length=100)

    def __str__(self):
        return self.archivo.name
