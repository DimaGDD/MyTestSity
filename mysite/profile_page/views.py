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
        if 'avatar' in request.FILES:
            avatar_form = AvatarUploadForm(request.POST, request.FILES, instance=request.user)

            old_avatar = request.user.avatar
            old_avatar.delete()
    
            if avatar_form.is_valid():
                avatar_form.save()
                return redirect('profile_page')

        elif 'delete_avatar' in request.POST:
            if request.user.avatar:
                request.user.avatar.delete()
            return redirect('profile_page')
    
    return render(request, 'profile_page/profile.html', {'form': form, 'user': request.user})