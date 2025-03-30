from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Required for password input but not displayed
    token = serializers.CharField(read_only=True)     # Token should be returned after user creation

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'password', 'token']

    def create(self, validated_data):
        # Create user using the create_user() method
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        # Generate a token for the new user
        token, created = Token.objects.get_or_create(user=user)

        # Include token in the validated data
        validated_data['token'] = token.key

        return user

