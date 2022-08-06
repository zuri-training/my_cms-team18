from pyexpat import model
from django.contrib import admin
from .models import UserProfile, Page, Template, Category, Style, Script

class StyleAdmin(admin.StackedInline):
    model = Style

class ScriptAdmin(admin.StackedInline):
    model = Script

class TemplateAdmin(admin.ModelAdmin):
    inlines = [StyleAdmin, ScriptAdmin]
    class Meta:
        model = Template

@admin.register(Style)
class StyleAdmin(admin.ModelAdmin):
    pass

@admin.register(Script)
class ScriptAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile)
admin.site.register(Page)
admin.site.register(Template, TemplateAdmin)
admin.site.register(Category)
