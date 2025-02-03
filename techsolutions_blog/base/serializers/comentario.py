from rest_framework import serializers
from ..models import Comentario

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comentario
        fields = ['conteudo']

    def create(self, validated_data):
        postagem = self.context['postagem']
        autor = self.context['request'].user
        comentario = Comentario.objects.create(postagem=postagem, autor=autor, **validated_data)
        return comentario