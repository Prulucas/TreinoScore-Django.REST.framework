from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

User = get_user_model()


class CustomUserCreateForm(UserCreationForm):

    class Meta:
        model = User

        fields = (
            'first_name',
            'last_name',
            'email',
            'cpf',
            'role'
        )


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError(
                "Este e-mail já está em uso por outro usuário.")
        return email
