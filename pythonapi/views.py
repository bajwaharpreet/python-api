from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET", "POST"])
def first_api(request):
    return Response({
        "Message" : "This is my first get API",
        "data" : "this is all data"
    })