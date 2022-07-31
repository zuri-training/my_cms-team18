from django.contrib.auth.models import User

def registration_validation(username, password, password1):
    errors = {}
    if User.objects.filter(username=username).exists():
            errors['username'] = 'Username already exists'
    if len(password) < 8:
        errors['password'] = 'Password must have a minimum of 8 characters' 
    elif password != password1:
        errors['password'] = 'Password mismatch'
    return errors