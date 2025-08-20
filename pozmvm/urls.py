from django.urls import path
from .views import UploadEntryAPIView

urlpatterns = [
    path('file-upload/', UploadEntryAPIView.as_view(), name='file-upload'),

]

