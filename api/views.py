from django.shortcuts import render
#
# # Create your views here.
# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
#
from api.models import MovieModel
from api.serializers import MovieSerializer
#
#
# class MovieView(APIView):
#     def get(self, request, *args, **kwargs):
#         movies = MovieModel.objects.all()
#         data = MovieSerializer(movies, many=True).data
#         return Response(data, status=status.HTTP_200_OK)
#
#     def post(self, request, *args, **kwargs):
#         movie = MovieSerializer(data=request.data)
#         if not movie.is_valid():
#             return Response(movie.errors)
#         movie.save()
#         return Response(movie.data, status=status.HTTP_201_CREATED)
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


class MovieView(ListCreateAPIView):
    serializer_class = MovieSerializer
    # queryset = MovieModel.objects.all()

    def get_queryset(self):
        request = self.request
        queryset = MovieModel.objects.all()
        params = request.query_params.get('name')
        if params:
            return queryset.filter(title__icontains=params)
        return queryset


class MovieDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = MovieModel.objects.all()
