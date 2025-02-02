from rest_framework import serializers
from .models import Postagem
from .serializers_user import UserSerializer

class PostagemSerializer(serializers.ModelSerializer):
    autor = UserSerializer(read_only=True)

    class Meta:
        model = Postagem
        fields = ['id', 'titulo', 'data_postagem', 'autor', 'imagem', 'slug', 'artigo']
