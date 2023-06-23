from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework import permissions
from apps.users.permissions import IsOwnerOrReadOnly

class PostListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    def get_queryset(self):
        queryset = Post.objects.all()
        user_id = self.request.query_params.get('user_id', None)
        if user_id is not None:
            queryset = queryset.filter(owner_id=user_id)
        return queryset
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class PostRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDestroyAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, permissions.IsAuthenticated]