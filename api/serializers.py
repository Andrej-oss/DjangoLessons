from rest_framework.serializers import ModelSerializer

from api.models import MovieModel


class MovieSerializer(ModelSerializer):
    class Meta:
        model = MovieModel
        fields = '__all__'
