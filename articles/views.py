from django.shortcuts import render
from rest_framework.response import Response
from users.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from articles.models import Article
from articles.serializers import (
    ArticleSerializer,
    ArticleListSerializer,
    ArticleCreateSerializer,
)


class ArticleView(APIView):
    def get(self, request):
        article_list = Article.objects.all()
        serializer = ArticleListSerializer(article_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ArticleCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"message": f"{serializer.errors}"}, status=status.HTTP_400_BAD_REQUEST
            )


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
