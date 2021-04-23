from django.shortcuts import render

# view using render()


def index(request):
    return render(request, 'index.html')
