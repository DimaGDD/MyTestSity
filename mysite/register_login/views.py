from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


def index(request):
	return HttpResponse("Хуй!")


def sign_up(request):
	if request.method == 'POST':
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			return redirect('/')
	else:
		form = UserRegisterForm()

	return render(request, 'register_login/register.html', { 'form' : form })