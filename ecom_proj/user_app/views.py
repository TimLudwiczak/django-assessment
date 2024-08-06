from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, login, logout

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token 
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.status import ( HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST )


# Create your views here.
class Sign_Up(APIView):
    def post(self, request):
        
class Log_in(APIView):
    pass

class Log_out(APIView):
    pass