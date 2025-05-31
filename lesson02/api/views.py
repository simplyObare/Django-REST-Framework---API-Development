from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET"])
def product_list(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response(serializer.data)


@api_view(["GET"])
def product_details(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)

    return Response(serializer.data)
