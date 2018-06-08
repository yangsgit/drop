from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import LoginForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import Profile



def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('blog:user_home',)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('账号不存在或密码错误')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('account:login',)


def user_profile(request, username):
    user = request.user
    if request.method == 'POST':
        intro = request.POST['intro']
        img = request.FILES['portrait']
        if not hasattr(user, 'profile'):
            profile = Profile()
            profile.user = user
        user.profile.intro = intro
        portraitName = user.username + '_' + 'portrait'
        user.profile.portrait.save(portraitName, img)
        user.save()
    else:
        profile_form = ProfileForm()

    return render(request,
                  "account/profile.html",
                  {
                      "user": user,
                  }
                  )



def user_register(request):
    if request.method == 'POST':
        postdic = request.POST
        username = postdic['username']
        password = postdic['password']
        affirm = postdic['affirm']
        email = postdic['email']
        if password == affirm:
            user = User.objects.create_user(username, email, affirm)
            user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('blog:user_home',)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('账号不存在或密码错误')
        else:
            return HttpResponse('两次密码输入不同')
    else:
        return render(request, 'account/register.html',)
