from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm, LoginForm


def sign_up(request):

	if request.user.is_authenticated:
		return redirect('home_page')

	form = CreateUserForm()

	if request.method == 'POST':
		form = CreateUserForm(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			password = form.cleaned_data.get('password1')
			user.set_password(password)
			user.save()

			messages.success(request, 'Аккаунт создан успешно!')

			user = authenticate(request, email=user.email, password=password)
			if user is not None:
				login(request, user)

			return redirect('home_page')

	return render(request, 'register_login/register.html', {'form' : form})


def sign_in(request):

	if request.user.is_authenticated:
		return redirect('home_page')

	form = LoginForm()

	if request.method == 'POST':
		form = LoginForm(data=request.POST)

		if form.is_valid():

			email = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')

			print(email, password)

			user = authenticate(request, email=email, password=password)

			if user is not None:
				login(request, user)

				return redirect('home_page')

	return render(request, 'register_login/login.html', {'form' : form})

@login_required
def user_logout(request):
	logout(request)

	return redirect('home_page')