from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class MainView(APIView): # class kotory bydem otobrajat
    def get(self, request):
        return Response({})

class SumView(APIView):
    def get(self, request):
        query = request.GET
        print()
        return Response({'res': ''})

    def post(self, request):
        pass
