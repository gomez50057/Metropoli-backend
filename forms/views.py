from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import Acuerdo, Actualizacion
from .serializers import AcuerdoSerializer, ActualizacionSerializer, AcuerdoCargaMasivaSerializer

class AcuerdoViewSet(viewsets.ModelViewSet):
    queryset = Acuerdo.objects.all()
    serializer_class = AcuerdoSerializer

class ActualizacionViewSet(viewsets.ModelViewSet):
    queryset = Actualizacion.objects.all()
    serializer_class = ActualizacionSerializer

class AcuerdoCargaMasivaViewSet(viewsets.ViewSet):
    def create(self, request):
        if isinstance(request.data, list):
            # Si es una lista, procesamos cada uno de los elementos
            serializer = AcuerdoCargaMasivaSerializer(data=request.data, many=True)
        else:
            # Si es un diccionario, lo procesamos normalmente
            serializer = AcuerdoCargaMasivaSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.db.models import Count
from rest_framework.views import APIView

class DashboardStatsView(APIView):
    """
    API para obtener estadísticas de los acuerdos y actualizaciones en la Dashboard.
    """

    def get(self, request, format=None):
        # 1. Contar el total de acuerdos
        total_acuerdos = Acuerdo.objects.count()

        # 2. Contar acuerdos por comisión
        acuerdos_por_comision = Acuerdo.objects.values('comision').annotate(total=Count('id_unico'))

        # 3. Contar acuerdos por Zona Metropolitana (ZM)
        acuerdos_por_zm = Acuerdo.objects.values('zm').annotate(total=Count('id_unico'))

        # 4. Contar acuerdos por estatus
        acuerdos_por_estatus = Acuerdo.objects.values('estatus').annotate(total=Count('id_unico'))

        # 5. Contar acuerdos por estatus y ZM
        acuerdos_por_estatus_zm = Acuerdo.objects.values('zm', 'estatus').annotate(total=Count('id_unico'))

        # 6. Contar total de actualizaciones
        total_actualizaciones = Actualizacion.objects.count()

        # 7. Contar actualizaciones por estado
        actualizaciones_por_estado = Actualizacion.objects.values('estado').annotate(total=Count('id'))

        # Construcción del JSON de respuesta
        data = {
            "acuerdos": {
                "total": total_acuerdos,
                "por_comision": list(acuerdos_por_comision),
                "por_zm": list(acuerdos_por_zm),
                "por_estatus": list(acuerdos_por_estatus),
                "por_estatus_zm": list(acuerdos_por_estatus_zm),
            },
            "actualizaciones": {
                "total": total_actualizaciones,
                "por_estado": list(actualizaciones_por_estado),
            }
        }

        return Response(data)
