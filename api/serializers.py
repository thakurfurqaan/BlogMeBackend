from rest_framework import serializers
from .models import Post
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token


# class ArticleSerializer(serializers.ModelSerializer):
#     # _id = serializers.IntegerField(source='id')
#     # renamed_name = serializers.CharField(source='')

#     class Meta:
#         model = Article
#         fields = ["userId","id","title", "body"]

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["userId","id","title", "body"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]

        extra_kwargs = {
            'password': {
                'write_only': True,
                'required': True,
            }
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user