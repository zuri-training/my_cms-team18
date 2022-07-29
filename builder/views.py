from django.shortcuts import render
from django.http import JsonResponse
from .models import Template, UserProfile, Page
from django.core.serializers import serialize
import json
from django.contrib.auth import authenticate, login, logout

def index(request):
    templates = Template.objects.all()
    return render(request, 'home.html', context={'templates': templates})

def preview_template(request, id):
    temp_obj = Template.objects.get(id=id)
    return render(request, 'preview.html', context={'template': temp_obj})

def edit_template(request, id):
    temp_obj = Template.objects.get(id=id)
    return render(request, 'edit.html', context={'template': temp_obj})

def save_template(request, id):
    thumbnail = Template.objects.get(id=id).thumbnail
    user = UserProfile.objects.get(user=request.user)
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        title = request.POST['title']
        page = Page.objects.create(
            user=user,
            title=title,
            html=html,
            css=css,
            thumbnail=thumbnail
        )
        page.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [page])))[0]})

def user_templates(request, username):
    user = UserProfile.objects.get(user=request.user)
    templates = Page.objects.all().filter(user=user)
    return render(request, 'user_templates.html', context={'templates': templates})

def user_template_preview(request, username, id):
    temp_obj = Page.objects.get(id=id)
    return render(request, 'preview.html', context={'template': temp_obj})

def edit_user_template(request,username,  id):
    temp_obj = Page.objects.get(id=id)
    return render(request, 'edit_user_template.html', context={'template': temp_obj})

def save_user_template(request,username,  id):
    user = UserProfile.objects.get(user=request.user)
    if(request.method=='POST'):
        html = request.POST['html']
        css = request.POST['css']
        title = request.POST['title']
        page = Page.objects.get(user=user, id=id)
        page.title=title
        page.html=html
        page.css=css
        page.save()
    return JsonResponse({ "result" : (json.loads(serialize('json', [page])))[0]})


