from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login


@csrf_exempt
def index(request):
    if not request.user.is_authenticated:
        return redirect('/login')

    return render(request, 'frontend/index.html')


@csrf_exempt
def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')

    return render(request, 'frontend/login.html')
