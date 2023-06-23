from .models import *
from rest_framework import serializers



class PostSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(slug_field='username', read_only=True)
    class Meta:
        model = Post
        fields = '__all__'
