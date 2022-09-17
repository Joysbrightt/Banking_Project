from django.shortcuts import render
from django.http import HttpResponse
from .serializer import CustomerSerializer
from .models import *
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def customer(request, format=None):
    if request.method == 'GET':
        customer = Customer.objects.all()
        serializer = CustomerSerializer(customer, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def createCustomer(request,format=None):
    if request.method == 'POST':
        customer = CustomerSerializer(data=request.data)
        if Customer.objects.filter(**request.data).exists():
            raise serializers.ValidationError("Sorry, this customer already exist")

        if customer.is_valid():
            customer.save()
            return Response(customer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
