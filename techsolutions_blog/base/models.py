import uuid

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class Postagem(models.Model):
    titulo = models.CharField(max_length=100)
    data_postagem = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="postagens")
    imagem = models.ImageField(upload_to='postagens', blank=True, null=True)
    artigo = models.TextField(max_length=4000)
    slug = models.SlugField(unique=True, blank=True, null=True)

    class Meta:
        ordering = ["-data_postagem"]


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.titulo)}-{uuid.uuid4()}"
        super(Postagem, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    postagem = models.ForeignKey("base.Postagem", on_delete=models.CASCADE, related_name="comentarios")
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor} em {self.postagem}"