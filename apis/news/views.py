from django.shortcuts import render
from rest_framework.views import APIView
from apis.news.models import News, NewsComment
from apis.news.serializers import NewsSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, permission_classes
import jwt
from django.conf import settings

# Create your views here.

class NewsApiView(APIView):
    permission_classes= [IsAuthenticatedOrReadOnly]
    def get(self, request):
        news_list = News.objects.all()
        serializer = NewsSerializer(news_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



    def post(self, request):
        news_data = request.data
        news_data['author'] = request.META.get("HTTP_AUTHORIZATION")
        decode_user = jwt.decode(token, settings.SECRET_KEY, algorithms= ['HS256'])
        news_data['author'] = decode_user.get('user_id')
        serializer = NewsSerializer(data=news_data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)
            else:
                return Response(serializer.errors)

        