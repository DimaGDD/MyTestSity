from django import forms
from register_login.models import User

class AvatarUploadForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar']