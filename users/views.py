from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from users.forms import SignUpForm


def logout_view(request):
    context = {'msg': 'You have been successfully logged out.'}
    logout(request)
    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.account_type = form.cleaned_data.get('account_type')
            user.profile.specialization = form.cleaned_data.get('specialization')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
