from django.contrib import admin
from django.urls import path,include
from .views import hasta_login, hasta_signup,patientdash,doktor_login,doktor_signup,doctordash,randevu_sil,update_patient,update_doctor,randevu_guncelle,detail,drandevu_sil,drandevu_guncelle,rapor_sil,rapor_guncelle,rapor_indir,rapor_yukle,drapor_sil,drapor_guncelle,drapor_indir,admin_login,admin_signup,admindash


urlpatterns = [
    path('hasta_signup/',hasta_signup,name='hasta_signup'),
    path('hasta_login/',hasta_login,name='hasta_login'),
    path('patiendash/',patientdash,name='patientdash'),
    path('admindash/',admindash,name='admindash'),
    path('admin_signup/',admin_signup,name='admin_signup'),
    path('admin_login/',admin_login,name='admin_login'),
    path('doktor_signup/',doktor_signup,name='doktor_signup'),
    path('doktor_login/',doktor_login,name='doktor_login'),
    path('doctordash/',doctordash,name='doctordash'),
    path('randevu/sil/<int:randevu_id>/', randevu_sil, name='randevu_sil'),
    path('drandevu/sil/<int:randevu_id>/', drandevu_sil, name='drandevu_sil'),
    path('randevu/güncelle/<int:randevu_id>/', randevu_guncelle, name='randevu_guncelle'),
    path('drandevu/güncelle/<int:randevu_id>/', drandevu_guncelle, name='drandevu_guncelle'),
    path('hasta/guncelle/', update_patient, name='update_patient'),
    path('doktor/guncelle/', update_doctor, name='update_doctor'),
    path('doktor/detail/<int:id>', detail, name='detail'),
    path('rapor/<int:rapor_id>/sil/', rapor_sil, name='rapor_sil'),
    path('drapor/<int:rapor_id>/sil/', drapor_sil, name='drapor_sil'),
    path('rapor/<int:rapor_id>/guncelle/', rapor_guncelle, name='rapor_guncelle'),
    path('drapor/<int:rapor_id>/guncelle/', drapor_guncelle, name='drapor_guncelle'),
    # path('rapor/<int:rapor_id>/indir/', rapor_indir, name='rapor_indir'),
    path('rapor/<int:rapor_id>/indir/', rapor_indir, name='rapor_indir'),
    path('drapor/<int:rapor_id>/indir/', drapor_indir, name='drapor_indir'),
    path('rapor/yukle/', rapor_yukle, name='rapor_yukle'),

]