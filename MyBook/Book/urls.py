from .views import *
from django.urls import path, include
from rest_framework import routers


router= routers.SimpleRouter()
router.register(r'users', UserViewSet, basename='users'),
router.register(r'authors', UserViewSet, basename='authors'),
router.register(r'genre', UserViewSet, basename='genre'),
router.register(r'book', UserViewSet, basename='book'),
router.register(r'booklanguages', UserViewSet, basename='booklanguages'),
router.register(r'rating', UserViewSet, basename='rating'),
router.register(r'favorite', UserViewSet, basename='favorite'),
router.register(r'favoritebook', UserViewSet, basename='favoritebook'),
router.register(r'quote', UserViewSet, basename='quote'),


urlpatterns = [
    path('', include(router.urls)),
]