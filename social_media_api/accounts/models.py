from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)

    def __str__(self):
        return self.username

    def follow(self, user):
        """Follow another user"""
        if user != self:
            self.following.add(user)

    def unfollow(self, user):
        """Unfollow a user"""
        if user != self:
            self.following.remove(user)

    def is_following(self, user):
        """Check if the current user is following another user"""
        return self.following.filter(id=user.id).exists()

