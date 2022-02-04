from django.db.models import fields
from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, StringRelatedField
from .models import Authors, Biography, Book

class AuthorModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Authors
        fields = '__all__'

class BookModelSerializer(ModelSerializer):
    author = AuthorModelSerializer(many=True)
    class Meta:
        model = Book
        fields = '__all__'

class BiographyModelSerializer(ModelSerializer):

    class Meta:
        model = Biography
        fields = '__all__'