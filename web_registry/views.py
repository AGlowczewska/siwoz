from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    context = {}
    if request.user.profile.is_doctor():
        context['msg'] = "Doctor's portal"
    else:
        context['msg'] = "Patient's portal"

    return render(request, 'index.html', context)
