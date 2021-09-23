from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .serializers import LoginSerializer
from django.contrib.auth import login, logout
from rest_framework.authtoken.models import Token

class LoginView(APIView):
    def post(self, request):
        #post method
        serializer = LoginSerializer(data= request.data)
        serializer.is_valid(raise_exception= True)
        user = serializer.validated_data["user"]
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"Token": token.key}, status= 200)