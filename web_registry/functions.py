from users.models import *


def get_patient_list(doctor_username):
    query = Patient.objects.filter()
    patient_list = []
    for x in query:
        if x.doctor:
            temp_doctor = x.doctor.profile.user.username
        else:
            temp_doctor = None
        patient = {'username': x.profile.user.username, 'doctor': temp_doctor}
        if patient['doctor'] is None:
            patient['doctor'] = 'Not assigned'
            patient['action'] = 'Assign myself to the patient'  # todo other options
        elif patient['doctor'] == doctor_username:
            patient['action'] = 'Unassign myself from the patient'
        else:
            patient['action'] = 'Not permitted'
        patient_list.append(patient)
    return patient_list
