from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from car.models import CarModel


class CarSerializer(ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username')
