from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreateForm
from django.contrib import messages
from .forms import UserChangeForm


def register(request):

    if request.method == 'POST':
        form = CustomUserCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = CustomUserCreateForm()

    return render(request, 'registration/register.html', {
        'form': form
    })


@login_required
def user_dashbord(request):
    form = UserChangeForm(request.POST or None, instance=request.user)

    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Perfil  atualizado com sucesso!')
        return redirect('users:profile')
    context = {
        'form': form,
    }

    return render(request, 'users/profile.html', context)
