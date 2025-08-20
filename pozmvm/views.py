from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UploadEntrySerializer

class UploadEntryAPIView(APIView):
    def post(self, request):
        serializer = UploadEntrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'mensaje': 'Archivos subidos correctamente'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
