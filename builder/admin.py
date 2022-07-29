from django.contrib import admin
from .models import UserProfile, Page, Template

admin.site.register(UserProfile)
admin.site.register(Page)
admin.site.register(Template)

