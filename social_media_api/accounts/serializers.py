from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Ensuring password is write-only
    token = serializers.CharField(read_only=True)     # Token is read-only, as it is generated automatically

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'password', 'token']

    def create(self, validated_data):
        # Create the user with password
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        # Create token for the user
        token, created = Token.objects.get_or_create(user=user)

        # Include token in the validated data
        validated_data['token'] = token.key

        return user
