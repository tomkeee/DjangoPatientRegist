from django.urls import path
from django.conf.urls import url
from .views import patient_list_view, patient_create_view, patient_detail_view

urlpatterns=[
        path('list/',patient_list_view),
        path('',patient_list_view),
        path('<int:pk>/',patient_detail_view, name="patient-detail"),
        path("create/",patient_create_view),
]