from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    password = serializers.CharField(write_only=True)  # Required for password input but not displayed
    token = serializers.CharField(read_only=True)     # Token should be returned after user creation
=======
    password = serializers.CharField(write_only=True)  # Ensuring password is write-only
    token = serializers.CharField(read_only=True)     # Token is read-only, as it is generated automatically
>>>>>>> 23aaa208245a1a5cd88766c7b8cff276f0eacad1

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'password', 'token']

    def create(self, validated_data):
<<<<<<< HEAD
        # Create user using the create_user() method
=======
        # Create the user with password
>>>>>>> 23aaa208245a1a5cd88766c7b8cff276f0eacad1
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

<<<<<<< HEAD
        # Generate a token for the new user
=======
        # Create token for the user
>>>>>>> 23aaa208245a1a5cd88766c7b8cff276f0eacad1
        token, created = Token.objects.get_or_create(user=user)

        # Include token in the validated data
        validated_data['token'] = token.key

        return user
<<<<<<< HEAD

=======
>>>>>>> 23aaa208245a1a5cd88766c7b8cff276f0eacad1
