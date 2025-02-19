from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView



class ChatbotView(APIView):
    def post(self, request):
        return Response({'message': 'Hello, world!'},status=status.HTTP_200_OK)
