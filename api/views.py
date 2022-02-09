from ast import Delete
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from itsdangerous import Serializer

from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ArticleViewSet(viewsets.ModelViewSet):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)

'''
class ArticleViewSet(viewsets.ViewSet):

    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    
    def list(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    # def update(self, request, pk=None):
    #     queryset = Article.objects.all()
    #     serializer = ArticleSerializer(data=request.data)
    #     serializer = ArticleSerializer(self.get_object(id), data=request.data)

    #     if serializer.is_valid():
    #         serializer.save()

    #         return Response(serializer.data, status=status.HTTP_201_CREATED)

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    # def delete(self, request, id):
    #     self.get_object(id).delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT )

    


class ArticleList(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
    
class ArticleDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'id'
    
    def get(self, request, id):
        return self.retrieve(request, id=id)

    def put(self, request, id):
        return self.update(request, id=id)

    def delete(self, request, id):
        return self.destroy(request, id=id)
    

class ArticleList(APIView):

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetails(APIView):

    def get_object(self, id):
        try: 
            article = Article.objects.get(pk=id)
            return article
        except Article.DoesNotExist:
            return Response("Article Does not exists", status=status.HTTP_404_NOT_FOUND)
            
    def get(self, request, id):
        serializer = ArticleSerializer(self.get_object(id))
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def put(self, request, id):
            
        serializer = ArticleSerializer(self.get_object(id), data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, id):
        self.get_object(id).delete()
        return Response(status=status.HTTP_204_NO_CONTENT )
        



def index(request):
    return HttpResponse("It is working")

@api_view(["GET", "POST"])
def article_list(request):

    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)

        return Response(serializer.data)

    elif request.method == "POST":
        # data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def article_details(request, id):
    try: 
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        return Response("Article Does not exists", status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ArticleSerializer(article)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    elif request.method == "PUT":
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED, safe=False)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == "DELETE":
        article.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

'''