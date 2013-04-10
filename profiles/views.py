from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
@login_required
def show(request):
    return render(request, 'templates/show.html')


def new(request):
    return render(request, 'registration/new.html' )


def create(request):
    return render(request, 'templates/new.html')

