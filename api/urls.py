from email.mime import base
from django.contrib import admin
from django.urls import path, include
from .views import UserViewSet, upload, PostViewSet
from rest_framework.routers import DefaultRouter
from django.views.decorators.csrf import csrf_exempt

router = DefaultRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/upload/', csrf_exempt(upload)),
]