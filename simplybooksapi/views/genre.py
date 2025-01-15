from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooksapi.models import Genre


class GenreView(ViewSet):

    def retrieve(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        serializer = GenreSerializer(genre)
        return Response(serializer.data)

    def list(self, request):
        genre = Genre.objects.all()
        serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)

    def create(self, request):
        genre = Genre.objects.create(
            description=request.data["description"]
        )

        serializer = GenreSerializer(genre)
        return Response(serializer)

    def update(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        genre.description = request.data["description"]

        genre.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        genre = Genre.objects.get(pk=pk)
        genre.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            'description',
        )
