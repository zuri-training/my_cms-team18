from django.urls import path
from .views import faq, features, index, preview_template, edit_template, blank, account, contact, save_template, user_templates, user_template_preview, edit_user_template, save_user_template, login_user, register_user, logout_user

urlpatterns = [
    path('', index, name="index"),
    path('preview/<int:id>/', preview_template, name='preview'),
    path('edit/<int:id>/', edit_template, name='edit'),
    path('save/<int:id>/', save_template, name='save'),
    path('<str:username>/mytemplates/', user_templates, name='user_templates'),
    path('<str:username>/preview/<int:id>/', user_template_preview, name='user_template_preview'),
    path('<str:username>/edit/<int:id>/', edit_user_template, name='edit_user_template'),
    path('<str:username>/save/<int:id>/', save_user_template, name='save_user_template'),
    path('login/', login_user, name='login'),
    path('sign-up/', register_user, name='register'),
    path('logout/', logout_user, name="logout"),
    path('account/<str:username>/', account, name='account'),
    path('blank/', blank, name='blank'),
    path('contact/', contact, name='contact'),
    path('features/', features, name='features'),
    path('faq/',faq, name='faq'),

    
]