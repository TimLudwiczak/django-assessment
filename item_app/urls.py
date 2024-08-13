from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='item_list'),  # List all items
    path('<int:pk>/', views.ItemDetailView.as_view(), name='item_detail'),  # Detail view for a single item
]
