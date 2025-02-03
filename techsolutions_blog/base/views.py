from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import Postagem
from .serializers.comentario import ComentarioSerializer
from .serializers.postagem import PostagemSerializer
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

    def destroy(self, request, *args, **kwargs):
        postagem = self.get_object()
        if postagem.autor != self.request.user:
            return Response({"detail": "Você não tem permissão para excluir esta postagem."}, status=403)
        return super().destroy(request, *args, **kwargs)

    @action(detail=True, methods=['get'])
    def visualizar_postagem(self, request, pk=None):
        postagem = self.get_object()
        serializer = self.get_serializer(postagem)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], url_path='comentarios')
    def comentarios(self, request, slug=None):
        postagem = self.get_object()  # Aqui, pegamos a postagem usando o slug vindo da URL
        serializer = ComentarioSerializer(data=request.data, context={'request': request, 'postagem': postagem})

        if serializer.is_valid():
            comentario = serializer.save()  # O comentário será salvo com a postagem e o autor
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)