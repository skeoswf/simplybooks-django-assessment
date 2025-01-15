from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status

from simplybooksapi.models import (
    Book,
    Author
)


class BookView(ViewSet):

    def retrieve(self, request, pk):
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    def list(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)

    def create(self, request):
        author = Author.objects.get(pk=request.data["author"])

        book = Book.objects.create(
            title=request.data["title"],
            image=request.data["image"],
            price=request.data["price"],
            sale=request.data["sale"],
            description=request.data["description"],
            author=author
        )

        serializer = BookSerializer(book)
        return Response(serializer.data)

    def update(self, request, pk):

        book = Book.objects.get(pk=pk)
        book.title = request.data["title"]
        book.image = request.data["image"]
        book.price = request.data["price"]
        book.sale = request.data["sale"]
        book.description = request.data["description"]

        author = Author.objects.get(pk=request.data["author"])
        book.author = author
        book.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = (
            'title',
            'image',
            'price',
            'sale',
            'description',
            'author_id'
        )
