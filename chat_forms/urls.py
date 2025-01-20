from django.urls import path
from .views import (
    ChatFormCreateView,
    ChatFormListView,
    ChatFormDetailView,
    ChatFormUpdateView,
    ChatFormDeleteView,
)

urlpatterns = [
    path('create/', ChatFormCreateView.as_view(), name='chatform-create'),
    path('', ChatFormListView.as_view(), name='chatform-list'),
    path('<int:pk>/', ChatFormDetailView.as_view(), name='chatform-detail'),
    path('update/<int:pk>/', ChatFormUpdateView.as_view(), name='chatform-update'),
    path('delete/<int:pk>/', ChatFormDeleteView.as_view(), name='chatform-delete'),
]
