from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostSerializer


class TestView(APIView):
    def get(self, request, *args, **kwargs):
        data = {"name": "John", "age": 23}
        return Response(data)

    def post(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
