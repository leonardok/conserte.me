from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.validators import validate_email, validate_slug
from django.core.exceptions import ValidationError

import logging

# Create your views here.
@login_required
def show(request):
    return render(request, 'templates/show.html')


def new(request):
    return render(request, 'registration/new.html' )


def create(request):
    valid = True

    if request.method == 'POST':
        """ Validations """
        try:
            validate_slug( request.POST['username'] )
            if len( request.POST['username'] ) < 5: raise ValidationError('Nome de usuario deve ter no minimo 5 letras.')
        except ValidationError:
            messages.add_message(request, messages.ERROR, 'Nome de usuario invalido.')
            valid = False

        try:
            validate_email( request.POST['email'] )
        except ValidationError:
            messages.add_message(request, messages.ERROR, 'Email invalido.')
            valid = False

        if len ( request.POST['password'] ) < 1 or request.POST['password'] != request.POST['password_confirmation']:
            messages.add_message(request, messages.ERROR, 'Senha invalida ou senhas nao coincidem.')
            valid = False

        """ If messages is set is because some error occured """
        if not valid:
            return render(request, 'registration/new.html' )

        """ saves the user object """
        user = User.objects.create_user(request.POST['username'])
        user.email = request.POST['email']
        user.set_password( request.POST['password'] )

        user.save()
        logging.debug( request.POST )

    messages.add_message(request, messages.SUCCESS, 'Usuario cadastrado com sucesso.')
    return redirect('/')

