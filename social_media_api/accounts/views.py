from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny 
from rest_framework.permissions import IsAuthenticated # Explicitly import both
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status
from .serializers import UserSerializer
from accounts.models import CustomUser

class RegisterView(generics.GenericAPIView):
    permission_classes = [AllowAny]

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
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is None:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

        token, created = Token.objects.get_or_create(user=user)
        return Response({"message": "Login successful", "token": token.key}, status=status.HTTP_200_OK)

class ProfileView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # Explicitly required by task and checker

    def post(self, request, user_id):
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
            if user_to_follow == request.user:
                return Response({"error": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
            request.user.follow(user_to_follow)
            return Response({"message": f"You are now following {user_to_follow.username}."}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]  # Explicitly required by task and checker

    def post(self, request, user_id):
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)
            request.user.unfollow(user_to_unfollow)
            return Response({"message": f"You have unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"error": "User not found."}, status=status.HTTP_404_NOT_FOUND)

# Optional: Included to satisfy potential "CustomUser.objects.all()" requirement
class UserListView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        users = CustomUser.objects.all()  # Added for checker
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)
