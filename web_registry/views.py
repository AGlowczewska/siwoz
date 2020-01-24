from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from web_registry.functions import *
from web_registry.forms import *


@login_required
def new_entry(request):
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            entry = form.save()
            entry.patient = request.user.profile.patient
            entry.save()
            return redirect('index')
    else:
        form = EntryForm()
    return render(request, 'entry_form.html', {'form': form})


@login_required
def new_comment(request, patient_username, entry_id):
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save()
            comment.entry = Entry.objects.get(id=entry_id)
            comment.autor = request.user
            comment.save()
            if request.user.profile.is_doctor():
                return redirect('patient_view', patient_username)
            else:
                return redirect('index')
    else:
        form = CommentForm()

    return render(request, 'comment_form.html', {'form': form})


@login_required
def patient_view(request, patient_username, entry_id=''):
    if entry_id:
        entry = Entry.objects.get(id=entry_id)
        entry.is_acknowledged = True
        entry.save()

    context = {'patient_username': patient_username, 'patient_entries_n': [], 'patient_entries_r': []}
    for x in Entry.objects.filter(patient__profile__user__username=patient_username):
        comments = Comment.objects.filter(entry=x)
        comment_list = []
        for com in comments:
            comment_list.append({'date': com.date, 'autor': com.autor.username, 'value': com.value})
        if x.entry_type == 'N':
            context['patient_entries_n'].append({'name': x, 'is_acknowledged': str(x.is_acknowledged),
                                                 'id': x.id, 'comment_list': comment_list})
        else:
            context['patient_entries_r'].append({'name': x, 'is_acknowledged': str(x.is_acknowledged),
                                                 'id': x.id, 'comment_list': comment_list})
    return render(request, 'patient_view.html', context)


@login_required
def index(request):
    context = {}
    if request.user.profile.is_doctor():
        context['header'] = "Doctor's portal"
        context['patient_list'] = []
        for x in Patient.objects.filter(doctor=request.user.profile.doctor):
            if Entry.objects.filter(is_acknowledged=False, patient=x):
                context['patient_list'].append({'name': x.profile.user.username, 'has_new_entries': True})
            else:
                context['patient_list'].append({'name': x.profile.user.username, 'has_new_entries': False})
        return render(request, 'doctor_index.html', context)
    else:
        context['header'] = "Patient's portal"
        context['patient_entries_n'] = []
        context['patient_entries_r'] = []
        context['patient_username'] = request.user.username
        for x in Entry.objects.filter(patient=request.user.profile.patient):
            comments = Comment.objects.filter(entry=x)
            comment_list = []
            for com in comments:
                comment_list.append({'date': com.date, 'autor': com.autor.username, 'value': com.value})
            if x.entry_type == 'N':
                context['patient_entries_n'].append({'name': x, 'is_acknowledged': str(x.is_acknowledged),
                                                     'id': x.id, 'comment_list': comment_list})
            else:
                context['patient_entries_r'].append({'name': x, 'is_acknowledged': str(x.is_acknowledged),
                                                     'id': x.id, 'comment_list': comment_list})
        return render(request, 'patient_index.html', context)


@login_required
def assign_patients(request):
    context = {'patient_list': get_patient_list(request.user.username)}
    return render(request, 'patient_list.html', context)


def assign_doctor(request, patient_username):
    patient_object = User.objects.get(username=patient_username).profile.patient
    patient_object.doctor = request.user.profile.doctor
    patient_object.save()
    context = {'patient_list': get_patient_list(request.user.username)}
    return render(request, 'patient_list.html', context)


def unassign_doctor(request, patient_username):
    patient_object = User.objects.get(username=patient_username).profile.patient
    patient_object.doctor = None
    patient_object.save()
    context = {'patient_list': get_patient_list(request.user.username)}
    return render(request, 'patient_list.html', context)