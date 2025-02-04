from django.contrib import admin
from rest_framework.routers import DefaultRouter
from .base.views import PostagemViewSet
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'postagens', PostagemViewSet, basename='postagem')

urlpatterns = [
    path("admin", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]