from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from web_registry.functions import *


@login_required
def index(request):
    context = {}
    if request.user.profile.is_doctor():
        context['header'] = "Doctor's portal"
        context['patient_list'] = []
        for x in Patient.objects.filter(doctor=request.user.profile.doctor):
            print(x.profile.user.username)
            context['patient_list'].append(x.profile.user.username)
        return render(request, 'doctor_index.html', context)
    else:
        context['header'] = "Patient's portal"
        return render(request, 'patient_index.html', context)


@login_required
def assign_patients(request):
    context = {'patient_list': get_patient_list()}
    return render(request, 'patient_list.html', context)


def assign_doctor(request, patient_username):
    patient_object = User.objects.get(username=patient_username).profile.patient
    patient_object.doctor = request.user.profile.doctor
    patient_object.save()
    context = {'patient_list': get_patient_list()}
    return render(request, 'patient_list.html', context)

