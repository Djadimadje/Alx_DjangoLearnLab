from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

class RegisterSerializer(serializers.ModelSerializer):
<<<<<<< HEAD
    password = serializers.CharField(write_only=True)  # ✅ This ensures "serializers.CharField()"
=======
    password = serializers.CharField(write_only=True)
>>>>>>> 1c753533750fe628b660eb6a198f1943cdefb3e2

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
<<<<<<< HEAD
        user = User.objects.create_user(  # ✅ This ensures "get_user_model().objects.create_user"
=======
        user = User.objects.create_user(
>>>>>>> 1c753533750fe628b660eb6a198f1943cdefb3e2
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
<<<<<<< HEAD
        Token.objects.create(user=user)  # ✅ This ensures "Token.objects.create"
        return user

=======
        # Create token for the new user
        Token.objects.create(user=user)
        return user
>>>>>>> 1c753533750fe628b660eb6a198f1943cdefb3e2
