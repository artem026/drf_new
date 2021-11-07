from rest_framework.viewsets import ModelViewSet
from .models import Authors
from .serializers import AuthorModelSerializer

class AuthorModelViewSet(ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorModelSerializer