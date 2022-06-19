# from django.shortcuts import render
from django.shortcuts import HttpResponse
from rest_framework.views import APIView

# Create your views here.

def show_get(request):
    print('Query', request.GET)
    print('Body', request.GET)
    return HttpResponse()

def show_post(request):
    print(request.data)
    print('Query', request.GET)
    print('Body', request.POST)
    return HttpResponse()

class TestView(APIView):


    def post(self, request):
        print(request.data)
        print('Query', request.GET)
        print('Body', request.POST)
        return HttpResponse()
