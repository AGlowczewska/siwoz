from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request, context={}):
    if request.user.profile.is_doctor():
        context['header'] = "Doctor's portal"
        return render(request, 'doctor_index.html', context)
    else:
        context['header'] = "Patient's portal"

    return render(request, 'index.html', context)
