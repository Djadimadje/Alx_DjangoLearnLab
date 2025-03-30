from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated  # Explicitly imported
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from accounts.models import CustomUser
from posts.models import Post
from posts.serializers import PostSerializer

class RegisterView(generics.GenericAPIView):
    permission_classes = [AllowAny]  # Allows unauthenticated users to register

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(username=username).exists():
            return Response({"error": "Username already exists."}, status=status.HTTP_400_BAD_REQUEST)

        user = CustomUser.objects.create_user(username=username, email=email, password=password)
        token, created = Token.objects.get_or_create(user=user)

        return Response({"message": "User registered successfully", "token": token.key}, status=status.HTTP_201_CREATED)

class LoginView(generics.GenericAPIView):
    permission_classes = [AllowAny]  # Allows unauthenticated users to log in

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)
        return Response({"message": "Login successful", "token": token.key}, status=status.HTTP_200_OK)

class ProfileView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # Ensure user is authenticated to view profile

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class FollowUserView(APIView):  # Changed to APIView to enforce explicit permissions
    permission_classes = [IsAuthenticated]  # Ensuring authentication is required

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(CustomUser, id=user_id)
        if user_to_follow == request.user:
            return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
        request.user.follow(user_to_follow)
        return Response({"message": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)

class UnfollowUserView(APIView):  # Changed to APIView to enforce explicit permissions
    permission_classes = [IsAuthenticated]  # Ensuring authentication is required

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(CustomUser, id=user_id)
        request.user.unfollow(user_to_unfollow)
        return Response({"message": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)

class UserListView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # Ensure only authenticated users can view the list

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class UserFeedView(APIView):
    permission_classes = [IsAuthenticated]  # Only authenticated users can view their feed

    def get(self, request):
        followed_users = request.user.following.all()  # Get all users the current user follows
        posts = Post.objects.filter(author__in=followed_users).order_by('-created_at')  # Get their posts
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
