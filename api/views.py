from itsdangerous import Serializer
from .models import Post
from .serializers import  UserSerializer, PostSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import json


# Create your views here.

# class ArticleViewSet(viewsets.ModelViewSet):

#     serializer_class = ArticleSerializer
#     queryset = Article.objects.all()
#     # permission_classes = [IsAuthenticated]
#     # authentication_classes = (TokenAuthentication,)


class PostViewSet(viewsets.ModelViewSet):

    serializer_class = PostSerializer
    queryset = Post.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    # permission_classes = [IsAuthenticated]
    # authentication_classes = (TokenAuthentication,)

class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()

@api_view(['GET','POST'])
def upload(request):
    if(request.method == 'POST'):
        # req_body = json.loads(request.body)
        print("request:", request.body)
        # print("request:", request.data)
        return Response({"message": "Got some data!"})
    else:
        message = 'This is a testing message'
        return Response(data = message, status=status.HTTP_200_OK)