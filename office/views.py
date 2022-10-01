from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from office.models import OfficeModel, EmployeeModel
from office.serializers import OfficeSerializer, EmployeeSerializer


class OfficeView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        office_serializer = OfficeSerializer(data=data)
        if not office_serializer.is_valid():
            return Response(office_serializer.errors)
        office_serializer.save()
        return Response(office_serializer.data, status=status.HTTP_201_CREATED)

    def patch(self, *args, **kwargs):
        office = OfficeModel.objects.get(pk=1)
        office_serializer = OfficeSerializer(instance=office, data=self.request.data, partial=True)
        if not office_serializer.is_valid():
            return Response(office_serializer.errors)
        office_serializer.save()
        return Response(office_serializer.data, 201)
    
    def get(self, *args, **kwargs):
        # manager = OfficeModel.objects
        # query_set = manager.filter(city='gdansk')
        # return Response(OfficeSerializer(query_set, many=True), status=status.HTTP_200_OK)
        manager = EmployeeModel.objects
        # query_set = manager.filter(age__in=[20, 22, 28]).exclude(city='gdansk')
        query_set = manager.filter(office__name='sollers')
        return Response(EmployeeSerializer(query_set, many=True).data, status.HTTP_200_OK)
