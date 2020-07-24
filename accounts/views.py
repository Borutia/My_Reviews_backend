from django.shortcuts import render
from django.http import HttpResponse



from rest_framework.views import APIView
from rest_framework.response import Response

class Account_view(APIView):
    def get(self, request):
        pass
