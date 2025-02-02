from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Postagem
from .serializers import PostagemSerializer
from rest_framework.decorators import action


class PostagemViewSet(viewsets.ModelViewSet):
    queryset = Postagem.objects.all()
    serializer_class = PostagemSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'

    def perform_create(self, serializer):
        serializer.save(autor=self.request.user)

    def perform_update(self, serializer):
        postagem = self.get_object()
        if postagem.autor != self.request.user:
            return Response({"detail": "Você não tem permissão para editar esta postagem."}, status=403)
        serializer.save(autor=self.request.user)

    def perform_partial_update(self, serializer):
        postagem = self.get_object()
        if postagem.autor != self.request.user:
            return Response({"detail": "Você não tem permissão para editar esta postagem."}, status=403)
        serializer.save(autor=self.request.user)

    @action(detail=False, methods=['get'])
    def lista_postagens(self, request):
        postagens = self.queryset.all()
        serializer = self.get_serializer(postagens, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def visualizar_postagem(self, request, pk=None):
        postagem = self.get_object()
        serializer = self.get_serializer(postagem)
        return Response(serializer.data)
