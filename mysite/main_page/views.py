from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


# @login_required(login_url='sign_in')
def home_page(request):
	context = {'username': request.user.username}
	return render(request, 'main_page/index.html', context)