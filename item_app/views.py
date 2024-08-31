from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item, Cart
from .serializers import ItemSerializer
# Create your views here.
class All_items(APIView):
    def get(self, request):
        items = Item.objects.all()  
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data) 

class An_item(APIView):
     def get(self, request, item_id):
        try:
            items = Item.objects.all()
            serializer  = ItemSeralizer(items, many=True)
            return Response(serializer.data)
        except Item.DoesNotExist:
            return Response({"error": "Item not found"}, status=404)

class Item_by_category(APIView):