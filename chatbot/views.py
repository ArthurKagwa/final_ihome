from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file

class ChatbotView(APIView):
    def post(self, request):
        content = request.data.get('content')
        load_dotenv()
        client = OpenAI(

            api_key=os.getenv("OPENAI_API_KEY"),
            base_url="https://api.llama-api.com"
        )

        try:
            response = client.chat.completions.create(
                model="llama3.1-8b",
                messages=[
                    {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
                    {"role": "user", "content": content},
                ],
            )
            return Response(response.choices[0].message.content, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)