from django.shortcuts import render
from rest_framework import viewsets, status, generics
from .serializers import DomainsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Domain, Industry


# Create your views here.

# class DomainsViewSet(viewsets.ModelViewSet):
#     queryset = Domain.objects.all()
#     serializer_class = DomainsSerializer
#
#
# class DomainsView(APIView):
#     def get(self, request):
#         domain = [domains.name for domains in Domain.objects.all()]
#         return Response({'domain': domain})
#
#
# class IndustriesView(APIView):
#     def get(self, request):
#         industry = [industry.name for industry in Industry.objects.all()]
#         return Response({'industry': industry})
#
#
# class DomainDetailView(generics.RetrieveAPIView):
#     """View For The Details Of A Single Post"""
#
#     queryset = Domain.objects.all()
#     serializer_class = DomainsSerializer
#     lookup_field = ['slug', 'name', 'price']


class DomainList(generics.ListAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainsSerializer


class DomainDetail(generics.RetrieveAPIView):
    queryset = Domain.objects.all()
    serializer_class = DomainsSerializer
    lookup_field = 'slug'
