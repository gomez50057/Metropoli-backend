from rest_framework import serializers
from .models import ChatForm

class ChatFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatForm
        fields = '__all__'
