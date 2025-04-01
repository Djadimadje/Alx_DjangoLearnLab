from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for posts.
    """
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        If 'feed' action is requested, return posts from followed users.
        Otherwise, return all posts.
        """
        if self.action == 'feed' and self.request.user.is_authenticated:
            following_users = self.request.user.following.all()
            return Post.objects.filter(author__in=following_users).select_related('author').order_by('-created_at')
        return Post.objects.all().select_related('author').order_by('-created_at')

    def perform_create(self, serializer):
        """
        Automatically assigns the author when creating a post.
        """
        serializer.save(author=self.request.user)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def feed(self, request):
        """
        Retrieves posts from followed users.
        """
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).select_related('author').order_by('-created_at')
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

class CommentViewSet(viewsets.ModelViewSet):
    """
    Handles CRUD operations for comments.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Returns all comments, ordered by creation date.
        """
        return Comment.objects.all().select_related('author', 'post').order_by('-created_at')

    def perform_create(self, serializer):
        """
        Automatically assigns the author when creating a comment.
        """
        serializer.save(author=self.request.user)

    def has_object_permission(self, request, view, obj):
        """
        Restricts comment editing to the original author.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
