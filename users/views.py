from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from users.forms import SignUpForm
from users.models import Doctor, Patient, Profile


def logout_view(request):
    logout(request)
    return redirect('index')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = Profile.objects.create(user=user)
            user_profile.account_type = form.cleaned_data.get('account_type')
            user_profile.save()

            if user.profile.is_doctor():
                doctor = Doctor.objects.create(profile=user.profile,
                                               specialization=form.cleaned_data.get('specialization'))
                doctor.save()
            else:
                patient = Patient.objects.create(profile=user.profile)
                patient.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
