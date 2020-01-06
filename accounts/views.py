from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import auth, messages
from django import forms


class UserLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_invalid(self, form):
        messages.error(self.request, '로그인 실패', extra_tags='danger')
        return super().form_invalid(form)


def register(request):
    res_data = {}

    if request.method == 'POST':
        sname = request.POST['sname']
        username = request.POST['username']
        password = request.POST['password1']
        re_password = request.POST['password2']
        print(sname)
        if not(username and sname and password and re_password):
            res_data['error'] = '입력하지 않은 정보가 있습니다.'
            return render(request, 'registration/re_register.html', res_data)

        elif password != re_password:
            # return HttpResponse("비밀번호가 다름")
            res_data['error'] = '비밀번호가 다릅니다.'
            # print(res_data['error'])

            return render(request, 'registration/re_register.html', res_data)

        elif User.objects.filter(username=sname).exists():
            res_data['error'] = '이미 가입되어 있는 학번입니다.'
            return render(request, 'registration/re_register.html', res_data)

        else:
            user = User(
                username = username,
                sname = sname,
                password = make_password(password),
            )
            user.save()
            auth.login(request, user)
            # request.session['username'] = username
            return render(request, 'registration/register_done.html', context={'user':user})

    return render(request, 'registration/register.html')



def profile(request):
    if not request.user.is_authenticated:
        data = {'username': request.user, 'is_authenticated': request.user.is_authenticated}
    else:
        data = {'last_login': request.user.last_login, 'username': request.user.username,
                'password': request.user.password, 'is_authenticated': request.user.is_authenticated}

    return render(request, 'registration/profile.html', context={'data': data})


def login(request):
    res_data = {}

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not (username and password):
            res_data = {'error' : 'Please enter your StudentID and password.'}
            return render(request, 'registration/login_error.html', context={'res_data':res_data})

        else:
            user = User.objects.get(username=username)

            if check_password(password, user.password):
                context = {'user':user}
                auth.login(request, user)
                request.session['username'] = username

                return render(request, 'index.html', context)

            else:
                res_data = {'error': 'Please enter a valid login name and password.'}
                return render(request, 'registration/login_error.html', context={'res_data': res_data})

    return render(request, 'registration/login.html', res_data)

# def result(request):
#     return HttpResponse("result")

# def register(request):
#     if request.method == 'POST':
#         if request.POST['password1'] == request.POST['password2']:
#             user = User.objects.create_user(
#                 username=request.POST['username'], password=request.POST['password1']
#             )
#             sid = request.POST['sid']
#             profile = Profile(user=user, sid=sid)
#             profile.save()
#             auth.login(request, user)
#             return render(request, 'registration/register_done.html', {'new_user':user})
#         else:
#             return render(request, 'registration/register.html')
#
#     return render(request, 'registration/register.html')




    #     user = User.objects.get(pk=user_id)
    #
    #     user_form = RegisterForm(request.POST)
    #     if user_form.is_valid():
    #         new_user = user_form.save(commit=False)
    #         new_user.set_password(user_form.cleaned_data['password'])
    #         new_user.save()
    #         return render(request, 'registration/register_done.html', {'new_user': new_user})
    # else:
    #     user_form = RegisterForm()
    #
    # return render(request, 'registration/register.html', {'form': user_form})


