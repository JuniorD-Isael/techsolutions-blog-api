from rest_framework import serializers
from .models import Postagem

class PostagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postagem
        fields = ['titulo', 'data_postagem', 'autor', 'imagem', 'slug', 'artigo']
