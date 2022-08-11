from ensurepip import bootstrap
from re import template
from turtle import title
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .models import Template, UserProfile, Page
from django.core.serializers import serialize
from django.contrib.auth.models import User
import json
from django.contrib.auth import authenticate, login, logout
from .validator import registration_validation
from django.contrib.auth.decorators import login_required

def index(request):
    templates = Template.objects.all()[:6]
    return render(request, 'core/index.html', context={'templates': templates})

def features(request):
    return render(request, 'core/features.html')

def faq(request):
    return render(request, 'core/faq.html')

def preview_template(request, id):
    temp_obj = Template.objects.get(id=id)
    scripts = temp_obj.template_scripts.all()
    styles = temp_obj.template_styles.all()
    return render(request, 'preview.html', context={'template': temp_obj, 'scripts':scripts, 'styles':styles})


def edit_template(request, id):
    temp_obj = Template.objects.get(id=id)
    scripts = temp_obj.template_scripts.all()
    styles = temp_obj.template_styles.all()
    return render(request, 'edit.html', context={'template': temp_obj, 'scripts':scripts, 'styles':styles})

def save_template(request, id):
    if not request.user.username:
        return JsonResponse({ "url" : '/sign-up/?next=%s' % '/edit/3/'})
    template = Template.objects.get(id=id)
    thumbnail = template.thumbnail
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
            thumbnail=thumbnail,
            parent_template=template
        )
        page.save()
        return JsonResponse({ "result" : (json.loads(serialize('json', [page])))[0]})

@login_required
def user_templates(request, username):
    user = UserProfile.objects.get(user=request.user)
    templates = Page.objects.all().filter(user=user)
    return render(request, 'core/usertemplates.html', context={'templates': templates})

@login_required
def user_template_preview(request, username, id):
    user = UserProfile.objects.get(user=request.user)
    temp_obj = Page.objects.get(id=id, user=user)
    scripts = [] if not temp_obj.parent_template else temp_obj.parent_template.template_scripts.all()
    styles = [] if not temp_obj.parent_template else temp_obj.parent_template.template_styles.all() 
    return render(request, 'preview.html', context={'template': temp_obj, 'scripts':scripts, 'styles':styles})

@login_required
def edit_user_template(request,username,  id):
    user = UserProfile.objects.get(user=request.user)
    temp_obj = Page.objects.get(id=id, user=user)
    scripts = [] if not temp_obj.parent_template else temp_obj.parent_template.template_scripts.all()
    styles = [] if not temp_obj.parent_template else temp_obj.parent_template.template_styles.all() 
    return render(request, 'edit_user_template.html', context={'template': temp_obj, 'scripts':scripts, 'styles':styles})

@login_required
def delete_user_template(request,username,  id):
    user = UserProfile.objects.get(user=request.user)
    temp_obj = Page.objects.get(id=id, user=user)
    temp_obj.delete()
    return JsonResponse({ "result" : 'Succesfully deleted', 'status': 204})


@login_required
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

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST['checkbox']
        user = authenticate(request, username=username, password=password)
        if user is not None:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                return JsonResponse({ "result" : 'Login successful', 'status': 200}, status=200)
        else:
             return JsonResponse({ "result" : 'Invalid username or password', 'status': 401}, status=401)
    return render(request, 'signin.html')

def logout_user(request):
    logout(request)
    return redirect('index')

def register_user(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        errors = registration_validation(username, password, password1)
        if errors:
            return JsonResponse({ "result" : errors, 'status': 409}, status=409)
        else:
            user = User.objects.create(
                username=username,
                email=email
            )
            user.set_password(password1)
            user.save()
            user_profile = UserProfile.objects.create(
                user=user
            )
            user_profile.save()
            user = authenticate(request, username=username, password=password1)
            login(request, user)
            return JsonResponse({ "result" : 'Registration Successful', 'status': 201}, status=201)
            
    return render(request, 'signup.html')

@login_required
def blank(request):
    temp_obj = Template.objects.get(title="Blank Page")
    scripts = temp_obj.template_scripts.all()
    styles = temp_obj.template_styles.all()
    return render(request, 'edit.html', context={'template': temp_obj, 'scripts':scripts, 'styles':styles})

@login_required
def account(request, username):
    user = User.objects.get(username=username)
    return render(request, 'core/account.html', context={'user': user})

def contact(request):
    return render(request, 'core/contact.html')

@login_required
def user_edit_profile(request, username):
    user = User.objects.get(username=request.user.username)
    if request.method == "POST":
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return JsonResponse({ "result" : 'Saved Successful', 'status': 201}, status=201)

def templates(request):
    templates = Template.objects.all()[:6]
    return render(request, 'core/templates.html', context={'templates': templates})

def post(request):
    templates = Template.objects.all()
    return render(request, 'core/templates.html', context={'templates': templates})

def publish_page(request, username, id):
    user = UserProfile.objects.get(user=request.user)
    temp_obj = Page.objects.get(id=id, user=user)
    published_pages = Page.objects.filter(user=user, publish=True)
    for publish_page in published_pages:
        publish_page.publish = False
        publish_page.save()
    temp_obj.publish = True
    temp_obj.save()
    domain = request.META['HTTP_HOST']
    user.domain_name = f'http://{domain}/{user.user.username}.com'
    user.save()
    return JsonResponse({ "result" : 'Saved Successful', 'status': 200}, status=200)

def user_site_url(request, username):
    user = UserProfile.objects.get(user=request.user)
    temp_obj = Page.objects.filter(user=user, publish=True).first()
    scripts = [] if not temp_obj.parent_template else temp_obj.parent_template.template_scripts.all()
    styles = [] if not temp_obj.parent_template else temp_obj.parent_template.template_styles.all() 
    return render(request, 'preview.html', context={'template': temp_obj, 'scripts':scripts, 'styles':styles})

def postpage(request):
    return render(request, 'core/postpage.html')

def post_detail_page(request):
    return render(request, 'core/post_detail.html')

def termsofservice(request):
    return render(request, 'core/terms.html')