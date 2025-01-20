from rest_framework import generics
from .models import ChatForm
from .serializers import ChatFormSerializer

# Crear un formulario (Create)
class ChatFormCreateView(generics.CreateAPIView):
    queryset = ChatForm.objects.all()
    serializer_class = ChatFormSerializer

# Leer un formulario específico o listar todos (Read)
class ChatFormListView(generics.ListAPIView):
    queryset = ChatForm.objects.all()
    serializer_class = ChatFormSerializer

class ChatFormDetailView(generics.RetrieveAPIView):
    queryset = ChatForm.objects.all()
    serializer_class = ChatFormSerializer

# Actualizar un formulario existente (Update)
class ChatFormUpdateView(generics.UpdateAPIView):
    queryset = ChatForm.objects.all()
    serializer_class = ChatFormSerializer

# Eliminar un formulario (Delete)
class ChatFormDeleteView(generics.DestroyAPIView):
    queryset = ChatForm.objects.all()
    serializer_class = ChatFormSerializer
