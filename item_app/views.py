from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item, Cart
# Create your views here.
class All_items(APIView):
    def get(self, request):


class An_item(APIView):
    def get(self, request):


class Item_by_category(APIView):