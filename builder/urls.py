from re import template
from django.urls import path
from .views import about, activity, delete_user_template, privacy, faq, features, index, post_detail_page, postpage, preview_template, edit_template, blank, account, contact, publish_page, save_template, support, templates, termsofservice, user_edit_profile, user_site_url, user_templates, user_template_preview, edit_user_template, save_user_template, login_user, register_user, logout_user

urlpatterns = [
    path('', index, name="index"),
    path('preview/<int:id>/', preview_template, name='preview'),
    path('edit/<int:id>/', edit_template, name='edit'),
    path('save/<int:id>/', save_template, name='save'),
    path('<str:username>/mytemplates/', user_templates, name='user_templates'),
    path('<str:username>/preview/<int:id>/', user_template_preview, name='user_template_preview'),
    path('<str:username>/edit/<int:id>/', edit_user_template, name='edit_user_template'),
    path('<str:username>/delete/<int:id>/', delete_user_template, name='delete_user_template'),
    path('<str:username>/save/<int:id>/', save_user_template, name='save_user_template'),
    path('<str:username>/publish/<int:id>/', publish_page, name='publish_user_template'),
    path('login/', login_user, name='login'),
    path('sign-up/', register_user, name='register'),
    path('logout/', logout_user, name="logout"),
    path('account/<str:username>/', account, name='account'),
    path('blank/', blank, name='blank'),
    path('contact/', contact, name='contact'),
    path('features/', features, name='features'),
    path('faq/',faq, name='faq'),
    path('account/<str:username>/edit/', user_edit_profile, name="user_edit_profile"),
    path('templates/', templates, name="templates"),
    path('<str:username>.com/', user_site_url, name="user_site_url"),
    path('posts/', postpage, name="post_page"),
    path('post-detail/', post_detail_page, name="post_detail_page"),
    path('terms-of-service/', termsofservice, name="terms_page"),
    path('about/', about, name="about"),
    path('privacy/', privacy, name="privacy"),
    path('support/', support, name="support"),
    path('activity/', activity, name="activity"),
]