from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^assign/(?P<patient_username>[A-Za-z0-9]+)/$', views.assign_doctor, name='assign_doctor'),
    url(r'^unassign/(?P<patient_username>[A-Za-z0-9]+)/$', views.unassign_doctor, name='unassign_doctor'),
    path('new_entry/', views.new_entry, name='new_entry'),
    path('assign/', views.assign_patients, name='assign_patients'),
    path('', views.index, name='index'),
]
