from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import User
from django.contrib.auth import authenticate


class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'Логин'
        self.fields['email'].label = 'Email'
        self.fields['password1'].label = 'Пароль'
        self.fields['password2'].label = 'Подтверждение пароля'

        self.fields['username'].error_messages = {
            'required': "Обязательное поле!",
            'max_length': "Имя слишком длинное!",
        }
        self.fields['email'].error_messages = {
            'required': "Введите адрес электронной почты!",
            'invalid': "Введите корректный адрес электронной почты!",
            'unique': "Пользователь с таким адресом электронной почты уже существует!",
        }
        self.fields['password1'].error_messages = {
            'required': "Пароль обязателен!",
            'min_length': "Пароль слишком короткий. Он должен содержать не менее 8 символов!",
        }
        self.fields['password2'].error_messages = {
            'required': "Подтверждение пароля обязательно!",
            'invalid': "Пароли не совпадают!",
        }


    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['unique'])
        return email


    def clean_username(self):
        username = self.cleaned_data['username']
        return username


    def save(self, commit=True):
        # user = super().save(commit=False)

        # user.id = Gamers.objects.generate_user_id()

        # if commit:
        #     user.save()

        user = User.objects.create_user(
            email=self.cleaned_data['email'],
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password1']
        )

        return user


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


    class Meta:
        fields = ['username', 'password']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'Email'
        self.fields['password'].label = 'Пароль'

        self.fields['username'].error_messages = {
            'required': 'Введите адрес электронной почты!',
            'invalid': "Введите корректный адрес электронной почты!",
        }
        self.fields['password'].error_messages = {
            'required': "Введите пароль!",
        }


    def clean(self):
        # cleaned_data = super().clean()

        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            user = authenticate(self.request, email=email, password=password)
            if user is None:
                raise forms.ValidationError('Неверный Email или Пароль!')

        return self.cleaned_data