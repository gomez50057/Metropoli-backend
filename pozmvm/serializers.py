from rest_framework import serializers
from .models import UploadEntry, UploadFile
from .validators import validar_tipo_archivo

class UploadFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadFile
        fields = ['archivo']

class UploadEntrySerializer(serializers.ModelSerializer):
    archivos = serializers.ListField(
        child=serializers.FileField(validators=[validar_tipo_archivo]),
        write_only=True
    )

    class Meta:
        model = UploadEntry
        fields = [
            'id',
            'nombre',
            'descripcion',
            'nombre_contacto',
            'numero_contacto',
            'extension',
            'archivos',
        ]

    def create(self, validated_data):
        archivos = validated_data.pop('archivos')
        entry = UploadEntry.objects.create(**validated_data)
        for archivo in archivos:
            UploadFile.objects.create(entry=entry, archivo=archivo, tipo_archivo=archivo.content_type)
        return entry
