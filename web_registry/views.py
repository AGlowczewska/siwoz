from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    context = {}
    if request.user.profile.is_patient():
        context['msg'] = "Patient's portal"
    else:
        context['msg'] = "Doctor's portal"

    return render(request, 'index.html', context)
