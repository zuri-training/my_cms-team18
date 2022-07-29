from email.policy import default
from turtle import mode, title
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio =  models.TextField(blank=True, null=True)
    domain_name = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.user.username

class Page(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length=200)
    html = models.TextField()
    css = models.TextField()
    publish = models.BooleanField(default=False)
    thumbnail = models.ImageField(default=None)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Template(models.Model):
    title = models.CharField(blank=False, null=False, max_length=200)
    html = models.TextField(blank=True, null=True,)
    css = models.TextField(blank=True, null=True,)
    thumbnail = models.ImageField()
    number_of_uses = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


