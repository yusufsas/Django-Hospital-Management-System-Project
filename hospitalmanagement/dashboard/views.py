from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Hasta,Doktor,Randevu,TibbiRapor
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from .models import Randevu,AdminAcc
import zipfile
import os
from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
import json
from django.conf import settings
import zipfile
import os
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

def index(request):

    return render(request,'index.html')



def hasta_login(request):
    if request.method == 'POST':
        HastaID = request.POST.get('HastaID')
        try:
            hasta = Hasta.objects.get(HastaID=HastaID)
            # Hasta bulundu, oturumu başlat
            request.session['hasta_id'] = hasta.id
            return redirect('patientdash')
        except Hasta.DoesNotExist:
            error_message = "Geçersiz Hasta ID"
            return render(request, 'registrations/patientlogin.html', {'error_message': error_message})
    else:
        return render(request, 'registrations/patientlogin.html')
def hasta_signup(request):
    if request.method == 'POST':
        HastaID = request.POST.get('HastaID')
        Ad = request.POST.get('Ad')
        Soyad = request.POST.get('Soyad')
        DogumTarihi = request.POST.get('DogumTarihi')
        Cinsiyet = request.POST.get('Cinsiyet')
        TelefonNumarasi = request.POST.get('TelefonNumarasi')
        Adres = request.POST.get('Adres')

        # Yeni bir Hasta nesnesi oluştur
        yeni_hasta = Hasta(HastaID=HastaID, Ad=Ad, Soyad=Soyad, DogumTarihi=DogumTarihi, 
                          Cinsiyet=Cinsiyet, TelefonNumarasi=TelefonNumarasi, Adres=Adres)
        yeni_hasta.save()

        # Kullanıcı başarıyla kaydedildi, başka bir sayfaya yönlendirilebilir
        return redirect('hasta_login')
    else:
        return render(request, 'registrations/patientsignup.html')   
def doktor_login(request):
    if request.method == 'POST':
        DoktorID = request.POST.get('DoktorID')
        try:
            doktor = Doktor.objects.get(DoktorID=DoktorID)
            # Hasta bulundu, oturumu başlat
            request.session['doktor_id'] = doktor.id
            return redirect('doctordash')
        except Doktor.DoesNotExist:
            error_message = "Geçersiz Doktor ID"
            return render(request, 'registrations/doctorlogin.html', {'error_message': error_message})
    else:
        return render(request, 'registrations/doctorlogin.html')
    
def admin_login(request):
    if request.method == 'POST':
        Ad = request.POST.get('Ad')
        Password = request.POST.get('Password')
        try:
            admin = AdminAcc.objects.get(Ad=Ad,password=Password)
            # Hasta bulundu, oturumu başlat
            request.session['admin_id'] = admin.id
            return redirect('admindash')
        except AdminAcc.DoesNotExist:
            error_message = "Geçersiz admin ID"
            return render(request, 'registrations/adminlogin.html', {'error_message': error_message})
    else:
        return render(request, 'registrations/adminlogin.html')
def doktor_signup(request):
    if request.method == 'POST':
        DoktorID = request.POST.get('DoktorID')
        Ad = request.POST.get('Ad')
        Soyad = request.POST.get('Soyad')
        
        UzmanlikAlani = request.POST.get('UzmanlikAlani')
        CalistigiHastane = request.POST.get('CalistigiHastane')
        

        # Yeni bir Hasta nesnesi oluştur
        yeni_doktor = Doktor(DoktorID=DoktorID, Ad=Ad, Soyad=Soyad,
                          UzmanlikAlani=UzmanlikAlani,CalistigiHastane=CalistigiHastane)
        yeni_doktor.save()

        # Kullanıcı başarıyla kaydedildi, başka bir sayfaya yönlendirilebilir
        return redirect('doktor_login')
    else:
        return render(request, 'registrations/doctorsignup.html')   
def admin_signup(request):
    if request.method == 'POST':
        
        Ad = request.POST.get('Ad')
        Soyad = request.POST.get('Soyad')
        Password = request.POST.get('Password')
        
        
        

        # Yeni bir Hasta nesnesi oluştur
        yeni_admin = AdminAcc( Ad=Ad, Soyad=Soyad,
                          password=Password)
        yeni_admin.save()

        # Kullanıcı başarıyla kaydedildi, başka bir sayfaya yönlendirilebilir
        return redirect('admin_login')
    else:
        return render(request, 'registrations/adminsignup.html')   


def patientdash(request):
    hasta_id = request.session.get('hasta_id')
    # Hasta kimliğine göre hasta nesnesini al
    hasta = Hasta.objects.get(id=hasta_id)
    doktorlar = Doktor.objects.all()
    if request.method == 'POST':
        if 'form1_submit' in request.POST:
            DoktorId= request.POST.get('doktor[]')
            Tarih= request.POST.get('RandevuTarihi')
            Saat=request.POST.get('RandevuSaati')
            doktor=Doktor.objects.get(id=DoktorId)
            instance=Randevu.objects.create(RandevuTarihi =Tarih,RandevuSaati=Saat,Hasta=hasta,Doktor=doktor)
            instance.save()
        elif 'form2_submit' in request.POST:
            image = request.FILES.get('reportimg')
            içerik= request.POST.get('içerik')
            tarih=request.POST.get('tarih')
            DoktorId= request.POST.get('doktor[]')
            doktor=Doktor.objects.get(id=DoktorId)
            instance=TibbiRapor.objects.create(RaporTarihi =tarih,RaporIcerigi=içerik,RaporImage=image,Hasta=hasta,Doktor=doktor)
            instance.save()

            
    randevular=Randevu.objects.filter(Hasta=hasta)
    raporlar=TibbiRapor.objects.filter(Hasta=hasta)
    return render(request, 'patientdash.html', {'hasta': hasta,'doktorlar':doktorlar,'randevular':randevular,'raporlar':raporlar})



def doctordash(request):
    doktor_id = request.session.get('doktor_id')
    # Hasta kimliğine göre hasta nesnesini al
    doktor = Doktor.objects.get(id=doktor_id)
    randevular=Randevu.objects.filter(Doktor=doktor)
    benzersiz_hastalar = set()

# Her randevunun hasta nesnesini set'e ekleyin
    for randevu in randevular:
        benzersiz_hastalar.add(randevu.Hasta)

# Set'ten bir liste oluşturun (gerekirse)
    hastalar = list(benzersiz_hastalar)


    return render(request,'doctordash.html',{'doktor': doktor,'hastalar':hastalar,'randevular':randevular})

def admindash(request):
    admin_id = request.session.get('admin_id')
    # Hasta kimliğine göre hasta nesnesini al
    admin = AdminAcc.objects.get(id=admin_id)
    hastalar=Hasta.objects.all()
    doktorlar=Doktor.objects.all()


    if request.method == 'POST':
        if 'form1_submit' in request.POST:
            hastalar= request.POST.getlist('hastalar')
            Hasta.objects.filter(id__in=hastalar).delete()
            
        elif 'form2_submit' in request.POST:
            doktorlar= request.POST.getlist('doktorlar')
            Doktor.objects.filter(id__in=doktorlar).delete()
            
            


    return render(request,'admindash.html',{'hastalar':hastalar,'doktorlar':doktorlar})

@require_POST
def randevu_sil(request, randevu_id):
    randevu = get_object_or_404(Randevu, id=randevu_id)
    randevu.delete()
    return redirect(reverse('patientdash'))

@require_POST
def drandevu_sil(request, randevu_id):
    randevu = get_object_or_404(Randevu, id=randevu_id)
    randevu.delete()
    return redirect(reverse('doctordash'))

def drandevu_guncelle(request, randevu_id):
    randevu = get_object_or_404(Randevu, id=randevu_id)
    if request.method == 'POST':
        # Güncelleme formundan gelen verileri al
        randevu_tarihi = request.POST.get('randevu_tarihi')
        randevu_saati = request.POST.get('randevu_saati')
        # Güncelleme işlemini yap
        randevu.RandevuTarihi = randevu_tarihi
        randevu.RandevuSaati = randevu_saati
        randevu.save()
        return redirect('doctordash')
    return render(request, 'drandevu_guncelle.html', {'randevu': randevu})

def randevu_guncelle(request, randevu_id):
    randevu = get_object_or_404(Randevu, id=randevu_id)
    if request.method == 'POST':
        # Güncelleme formundan gelen verileri al
        randevu_tarihi = request.POST.get('randevu_tarihi')
        randevu_saati = request.POST.get('randevu_saati')
        # Güncelleme işlemini yap
        randevu.RandevuTarihi = randevu_tarihi
        randevu.RandevuSaati = randevu_saati
        randevu.save()
        return redirect('patientdash')
    return render(request, 'randevu_guncelle.html', {'randevu': randevu})

def update_doctor(request):
    doktor_id = request.session.get('doktor_id')
    # Hasta kimliğine göre hasta nesnesini al
    doktor = Doktor.objects.get(id=doktor_id)

    if request.method == 'POST':
        
        Ad = request.POST.get('Ad')
        Soyad = request.POST.get('Soyad')
        
        UzmanlikAlani = request.POST.get('UzmanlikAlani')
        CalistigiHastane = request.POST.get('CalistigiHastane')
        
        # Hasta kaydını al ve güncelle
        # hasta = get_object_or_404(Hasta, id=hasta_id)
        doktor.Ad = Ad
        doktor.Soyad = Soyad
        doktor.UzmanlikAlani = UzmanlikAlani
        doktor.CalistigiHastane = CalistigiHastane
        
        doktor.save()
        
        return redirect(reverse('doctordash'))  # Güncelleme sonrası yönlendirme
    return render(request, 'update_doctor.html')

def update_patient(request):
    hasta_id = request.session.get('hasta_id')
    # Hasta kimliğine göre hasta nesnesini al
    hasta = Hasta.objects.get(id=hasta_id)
    if request.method == 'POST':
        hasta_id = request.POST.get('HastaID')
        ad = request.POST.get('Ad')
        soyad = request.POST.get('Soyad')
        dogum_tarihi = request.POST.get('DogumTarihi')
        cinsiyet = request.POST.get('Cinsiyet')
        telefon_numarasi = request.POST.get('TelefonNumarasi')
        adres = request.POST.get('Adres')
        
        # Hasta kaydını al ve güncelle
        # hasta = get_object_or_404(Hasta, id=hasta_id)
        hasta.Ad = ad
        hasta.Soyad = soyad
        hasta.DogumTarihi = dogum_tarihi
        hasta.Cinsiyet = cinsiyet
        hasta.TelefonNumarasi = telefon_numarasi
        hasta.Adres = adres
        hasta.save()
        
        return redirect(reverse('patientdash'))  # Güncelleme sonrası yönlendirme
    return render(request, 'update_patient.html')


def detail(request,id):

    hasta=Hasta.objects.get(id=id)
    randevular=Randevu.objects.filter(Hasta=hasta)
    raporlar=TibbiRapor.objects.filter(Hasta=hasta)


    return render(request,'detail.html',{'hasta':hasta,'raporlar':raporlar,"randevular":randevular})

def rapor_sil(request, rapor_id):
    rapor = get_object_or_404(TibbiRapor, id=rapor_id)
    rapor.delete()
    return redirect('patientdash')  # Rapor listesinin bulunduğu sayfaya yönlendirin
def drapor_sil(request, rapor_id):
    rapor = get_object_or_404(TibbiRapor, id=rapor_id)
    rapor.delete()
    return redirect('doctordash')

def rapor_guncelle(request, rapor_id):
    rapor = get_object_or_404(TibbiRapor, id=rapor_id)
    if request.method == 'POST':
        image = request.FILES.get('reportimg')
        içerik= request.POST.get('içerik')
        tarih=request.POST.get('tarih')
        rapor.RaporImage=image
        rapor.RaporTarihi=tarih
        rapor.RaporIcerigi=içerik
        rapor.save()
        return redirect('patientdash')  # Rapor listesinin bulunduğu sayfaya yönlendirin
    return render(request, 'update_report.html')
def drapor_guncelle(request, rapor_id):
    rapor = get_object_or_404(TibbiRapor, id=rapor_id)
    if request.method == 'POST':
        image = request.FILES.get('reportimg')
        içerik= request.POST.get('içerik')
        tarih=request.POST.get('tarih')
        rapor.RaporImage=image
        rapor.RaporTarihi=tarih
        rapor.RaporIcerigi=içerik
        rapor.save()
        return redirect('doctordash')  # Rapor listesinin bulunduğu sayfaya yönlendirin
    return render(request, 'update_report.html')




def rapor_yukle(request):
    if request.method == 'POST':
        # AJAX isteğinden gelen verileri al
        doktorlar = json.loads(request.POST.get('doktorlar'))
        tarih = request.POST.get('tarih')
        rapor_resmi = request.FILES.get('raporResmi')
        icerik = request.POST.get('icerik')

        # Raporu kaydet
        rapor = TibbiRapor.objects.create(
            RaporIcerigi=icerik,
            RaporTarihi=tarih,
            RaporImage=rapor_resmi
        )

        # Seçilen doktorları rapora ekle
        for doktor_id in doktorlar:
            rapor.doktorlar.add(doktor_id)

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'fail'}, status=400)
    
def rapor_indir(request, rapor_id):
    rapor = get_object_or_404(TibbiRapor, id=rapor_id)
    
    zip_filename = f"rapor_{rapor_id}.zip"
    zip_filepath = os.path.join(settings.MEDIA_ROOT, zip_filename)

    with zipfile.ZipFile(zip_filepath, 'w') as zip_file:
        rapor_icerigi_filename = f"rapor_{rapor_id}.txt"
        zip_file.writestr(rapor_icerigi_filename, rapor.RaporIcerigi)
        
        if rapor.RaporImage:
            rapor_image_filepath = rapor.RaporImage.path
            zip_file.write(rapor_image_filepath, os.path.basename(rapor_image_filepath))

    with open(zip_filepath, 'rb') as zip_file:
        response = HttpResponse(zip_file.read(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename={zip_filename}'
    
    os.remove(zip_filepath)

    return response

def drapor_indir(request, rapor_id):
    rapor = get_object_or_404(TibbiRapor, id=rapor_id)
    
    zip_filename = f"rapor_{rapor_id}.zip"
    zip_filepath = os.path.join(settings.MEDIA_ROOT, zip_filename)

    with zipfile.ZipFile(zip_filepath, 'w') as zip_file:
        rapor_icerigi_filename = f"rapor_{rapor_id}.txt"
        zip_file.writestr(rapor_icerigi_filename, rapor.RaporIcerigi)
        
        if rapor.RaporImage:
            rapor_image_filepath = rapor.RaporImage.path
            zip_file.write(rapor_image_filepath, os.path.basename(rapor_image_filepath))

    with open(zip_filepath, 'rb') as zip_file:
        response = HttpResponse(zip_file.read(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename={zip_filename}'
    
    os.remove(zip_filepath)

    return response