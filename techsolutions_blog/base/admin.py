from django.contrib import admin
from .models import Postagem

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor','data_postagem')
    search_fields = ('titulo', 'autor_username')
    list_filter = ('data_postagem', 'autor')
