from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from simplybooksapi.models import Author


class AuthorView(ViewSet):

    def retrieve(self, request, pk):
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def list(self, request):
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return Response(serializer.data)

    def create(self, request):

        author = Author.objects.create(
            email=request.data["email"],
            first_name=request.data["firstName"],
            last_name=request.data["lastName"],
            image=request.data["image"],
            favorite=request.data["favorite"]
        )
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        author = Author.objects.get(pk=pk)
        author.email = request.data["email"]
        author.first_name = request.data["firstName"]
        author.last_name = request.data["lastName"]
        author.image = request.data["image"]
        author.favorite = request.data["favorite"]

        author.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        author = Author.objects.get(pk=pk)
        author.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = (
            'email',
            'first_name',
            'last_name',
            'image',
            'favorite'
        )
