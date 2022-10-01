from rest_framework.serializers import ModelSerializer

from office.models import EmployeeModel, OfficeModel


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = '__all__'


class OfficeSerializer(ModelSerializer):
    class Meta:
        model = OfficeModel
        fields = '__all__'
