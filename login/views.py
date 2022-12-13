from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer


class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = serializer.create(validated_data=serializer.validated_data, request=request)
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Loginview(APIView):
    permission_classes = ()
    def post(self, request):
        phone = request.data.get("phone")
        password = request.data.get("password")
        user = authenticate(phone=phone, password=password)
        if not user:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
        token, _ = Token.objects.get_or_create(user=user)
        print(_)
        user_get =User.objects.get(phone=request.data.get('phone'))
        user_data =UserSerializer(user_get).data
        user_data.update(token=token.key)
        return Response({"token": user_data})