from django.urls import path
from . import views

urlpatterns = [
    path('', views.ClientListView.as_view(), name='client_list'),  # List all clients
    path('<int:pk>/', views.ClientDetailView.as_view(), name='client_detail'),  # Detail view for a single client
]
