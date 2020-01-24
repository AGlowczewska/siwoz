from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^acknowledge/(?P<patient_username>[A-Za-z0-9]+)/(?P<entry_id>[A-Za-z0-9]+)/$', views.patient_view, name='patient_view'),
    url(r'^view/(?P<patient_username>[A-Za-z0-9]+)/$', views.patient_view, name='patient_view'),
    url(r'^assign/(?P<patient_username>[A-Za-z0-9]+)/$', views.assign_doctor, name='assign_doctor'),
    url(r'^unassign/(?P<patient_username>[A-Za-z0-9]+)/$', views.unassign_doctor, name='unassign_doctor'),
    path('new_entry/(?P<patient_username>[A-Za-z0-9]+)/', views.new_entry, name='new_entry'),
    url('new_comment/(?P<patient_username>[A-Za-z0-9]+)/(?P<entry_id>[A-Za-z0-9]+)/$', views.new_comment, name='new_comment'),
    path('assign/', views.assign_patients, name='assign_patients'),
    path('', views.index, name='index'),
]
