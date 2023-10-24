from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm,\
                    UserEditForm, ProfileEditForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully(вы прошли аутентификацию)')
                else:
                    return HttpResponse('Disabled account(отключенная учетная запись)')
            else:
                return HttpResponse('Invalid login(некорректный логин)')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})

@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section':'dashboard'})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            
            #создается новый пользователь, без его сохранения
            new_user = user_form.save(commit=False)
            
            #устанавливает пароль
            new_user.set_password(
                user_form.cleaned_data['password'])
            
            # сохраняем объект User
            new_user.save()
            return render(request,
                          'account/template/register_done.html',
                          {'new_user':new_user})                         
            # создает профиль пользователя
            Profile.objects.create(user=new_user)
            return render(request,
                          'account/register_done.html',
                          {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/template/register.html',
                  {'user_form':user_form})

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid:
            try:
                user_form.save()
                profile_form.save()
                messages.success(request, 'Profile updated '\
                             'successfully')
            except ValueError:
                messages.error(request, 'Error updating you profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form':user_form,
                   'profile_form': profile_form})
  