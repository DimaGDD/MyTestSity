from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import AvatarUploadForm


@login_required
def profile_page(request):
    form = AvatarUploadForm(instance=request.user)

    if request.method == 'POST':
        form = AvatarUploadForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile_page')
    
    return render(request, 'profile_page/profile.html', {'form': form, 'user': request.user})