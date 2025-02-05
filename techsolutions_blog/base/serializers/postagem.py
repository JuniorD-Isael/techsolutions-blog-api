from rest_framework import serializers
from techsolutions_blog.base.models import Postagem
from techsolutions_blog.base.serializers.user import UserSerializer

class PostagemSerializer(serializers.ModelSerializer):
    autor = UserSerializer(read_only=True)

    class Meta:
        model = Postagem
        fields = ['id', 'titulo', 'data_postagem', 'autor', 'imagem', 'slug', 'artigo']
