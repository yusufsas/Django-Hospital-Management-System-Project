from django.contrib import admin
from django.urls import path,include
from .views import hasta_login, hasta_signup,patientdash,doktor_login,doktor_signup,doctordash,randevu_sil,update_patient,update_doctor,randevu_guncelle


urlpatterns = [
    path('hasta_signup/',hasta_signup,name='hasta_signup'),
    path('hasta_login/',hasta_login,name='hasta_login'),
    path('patiendash/',patientdash,name='patientdash'),
    path('doktor_signup/',doktor_signup,name='doktor_signup'),
    path('doktor_login/',doktor_login,name='doktor_login'),
    path('doctordash/',doctordash,name='doctordash'),
    path('randevu/sil/<int:randevu_id>/', randevu_sil, name='randevu_sil'),
    path('randevu/güncelle/<int:randevu_id>/', randevu_guncelle, name='randevu_guncelle'),
    path('hasta/guncelle/', update_patient, name='update_patient'),
    path('doktor/guncelle/', update_doctor, name='update_doctor'),

]