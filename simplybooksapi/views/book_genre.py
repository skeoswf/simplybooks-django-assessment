from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from simplybooksapi.models import (
    BookGenre,
    Book,
    Genre
)


class BookGenreView(ViewSet):

    def retrieve(self, request, pk):
        book_genre = BookGenre.objects.get(pk=pk)
        serializer = BookGenreSerializer(book_genre)
        return Response(serializer.data)

    def list(self, request):
        book_genre = BookGenre.objects.all()
        serializer = BookGenreSerializer(book_genre, many=True)
        return Response(serializer.data)

    def create(self, request):

        book = Book.objects.get(pk=request.data["book"])
        genre = Genre.objects.get(pk=request.data["genre"])

        book_genre = BookGenre.objects.create(
            book=book,
            genre=genre
        )
        serializer = BookGenreSerializer(book_genre)
        return Response(serializer.data)

    def update(self, request, pk):
        book_genre = BookGenre.objects.get(pk=pk)

        book = Book.objects.get(pk=request.data["book"])
        genre = Genre.objects.get(pk=request.data["genre"])

        book_genre.book = book
        book_genre.genre = genre
        book_genre.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        book_genre = BookGenre.objects.get(pk=pk)
        book_genre.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class BookGenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookGenre
        fields = (
            'book',
            'genre'
        )
        depth = 1
