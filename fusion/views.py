from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    test_string = 'test'
    context = {'test_string': test_string}
    return render(request, 'fusion/index.html', context)


def about(request):
    return render(request, 'fusion/about.html')

def contacts(request):
    return render(request, 'fusion/contacts.html')
