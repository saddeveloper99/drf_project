from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from users.serializers import UserSerializer
from rest_framework import permissions

# Create your views here.
class UserView(APIView):
    def post(self, request):
       serializer = UserSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response({"message":"가입완료!"}, status=status.HTTP_200_OK)
       else:
           return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
class mockView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        user.is_admin = True
        return Response("get 요청")
    