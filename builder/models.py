from django.db import models
from django.contrib.auth import get_user_model
from allauth.account.signals import user_signed_up

User = get_user_model()

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    bio =  models.TextField(blank=True, null=True)
    domain_name = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(blank=False, null=False, max_length=200)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Categories"

class Template(models.Model):
    title = models.CharField(blank=False, null=False, max_length=200)
    html = models.TextField(blank=True, null=True,)
    css = models.TextField(blank=True, null=True,)
    category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    thumbnail = models.ImageField()
    number_of_uses = models.PositiveIntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Page(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(blank=False, null=False, max_length=200)
    html = models.TextField()
    css = models.TextField()
    publish = models.BooleanField(default=False)
    thumbnail = models.ImageField(default=None)
    parent_template = models.ForeignKey(Template, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

class Style(models.Model):
    template = models.ForeignKey(Template, related_name="template_styles", on_delete=models.CASCADE)
    link = models.CharField(blank=True, null=True, max_length=260)

    def __str__(self):
        return  self.template.title
class Script(models.Model):
    template = models.ForeignKey(Template, related_name="template_scripts", on_delete=models.CASCADE)
    link = models.CharField(blank=True, null=True, max_length=260)
    def __str__(self):
        return  self.template.title

def user_signed_up_receiver(request, user, **kwargs):
    user_profile = UserProfile.objects.create(
                user=user
            )
    user_profile.save()

user_signed_up.connect(user_signed_up_receiver, sender=User)


