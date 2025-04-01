from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    following = models.ManyToManyField(
        'self', 
        symmetrical=False, 
        related_name='followers', 
        blank=True
    )

    def __str__(self):
        return self.username

    def follow(self, user):
        """Follow a user if not already following."""
        if user != self and not self.is_following(user):
            self.following.add(user)

    def unfollow(self, user):
        """Unfollow a user if currently following."""
        if user != self and self.is_following(user):
            self.following.remove(user)

    def is_following(self, user):
        """Check if the current user follows another user."""
        return self.following.filter(id=user.id).exists()

    def get_followers_count(self):
        """Return the number of followers the user has."""
        return self.followers.count()

    def get_following_count(self):
        """Return the number of users this user is following."""
        return self.following.count()

