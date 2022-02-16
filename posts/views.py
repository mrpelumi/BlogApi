from rest_framework import viewsets
from .serializers import PostSerializer,UserSerializer
from .models import Post
from .permissions import IsAuthorOrReadOnly
from django.contrib.auth import get_user_model

class PostList(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserList(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

