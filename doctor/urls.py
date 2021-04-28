from django.urls import path
from django.conf.urls import url
from .views import doctor_list_view,doctor_detail_view,doctor_create_view

urlpatterns=[
        path('list/',doctor_list_view),
        path('',doctor_list_view),
        path('<int:id>',doctor_detail_view),
        path('create/',doctor_create_view),
]