from django.contrib import admin
from django.urls import path, include

# from .views import article_list, article_details

# from .views import ArticleList, ArticleDetails

from .views import ArticleViewSet, UserViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('articles', ArticleViewSet, basename='articles')
router.register('users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]