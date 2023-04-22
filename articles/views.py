from django.shortcuts import render
from rest_framework.response import Response
from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status


# Create your views here.
class ArticleView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "가입완료!"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": f"{serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST
            )

    def post(self, request):
        pass


class ArticleDetailView(APIView):
    def get(self, request, article_id):
        pass

    def put(self, request):
        pass

    def delete(self, request, article_id):
        pass


class CommentView(APIView):
    def get(self, request, article_id):
        pass

    def post(self, request):
        pass

class CommentDetailView(APIView):
    def put(self, request):
        pass

    def delete(self, request, article_id):
        pass

class LikeView(APIView):
    def post(self, request):
        pass