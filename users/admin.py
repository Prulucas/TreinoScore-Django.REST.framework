from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + (
        # Adicionei o cpf aqui
        ('Informações Adicionais', {'fields': ('role', 'cpf')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Informações Adicionais', {'fields': ('role', 'cpf')}),
    )
