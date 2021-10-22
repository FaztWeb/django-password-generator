from django.shortcuts import render
from django.http import HttpResponse
import random
# import string

# Create your views here.


def home(request):
    return render(request, 'generator/home.html', {'name': 'Fazt'})


def generatedPassword(request):

    generated_password = ''
    # generated_password = ''.join([random.choice(
    #     string.ascii_letters + string.digits + string.punctuation) for n in range(12)])

    characters = list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*(){}[]'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))

    length = int(request.GET.get('length', 10))

    for x in range(length):
        generated_password += random.choice(characters)


    return render(request, 'generator/password.html', {'password': generated_password})

def about(request):
    return render(request, 'generator/about.html')