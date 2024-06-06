from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Category, Post, Comment

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostListSerializer(serializers.ModelSerializer):
    class PostCategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = '__all__'

    class PostUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username',)

    category = PostCategorySerializer(read_only=True)
    user = PostUserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostListDetailSerializer(serializers.ModelSerializer):
    class PostCategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = '__all__'
            
    class PostUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')
            
    category = PostCategorySerializer(read_only=True)
    user = PostUserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user', 'category')


class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user',)


class CommentListSerializer(serializers.ModelSerializer):
    class CommentUserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')

    user = CommentUserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post', 'user')
