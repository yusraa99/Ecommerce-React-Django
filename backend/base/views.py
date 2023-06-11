from django.shortcuts import render
from django.http import JsonResponse
from .products import products
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes=[
        '/api/products/',
        '/api/products/create/',
        '/api/products/',
        

    ]
    return Response(routes)

@api_view(['GET'])
def getProducts(request):
    return JsonResponse(products, safe=False)