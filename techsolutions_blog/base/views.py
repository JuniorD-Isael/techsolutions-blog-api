from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Postagem
from .serializers import PostagemSerializer

class PostagemViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)
