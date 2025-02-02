from rest_framework.routers import DefaultRouter
from .base.views import PostagemViewSet
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'postagens', PostagemViewSet, basename='postagem')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', obtain_auth_token, name='api_token_auth'),
]
