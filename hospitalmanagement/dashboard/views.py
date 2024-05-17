from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Hasta,Doktor,Randevu,TibbiRapor
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.decorators.http import require_POST
from .models import Randevu


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
        except Hasta.DoesNotExist:
            error_message = "Geçersiz Doktor ID"
            return render(request, 'registrations/doctorlogin.html', {'error_message': error_message})
    else:
        return render(request, 'registrations/doctorlogin.html')
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


def patientdash(request):
    
        


    hasta_id = request.session.get('hasta_id')
    # Hasta kimliğine göre hasta nesnesini al
    hasta = Hasta.objects.get(id=hasta_id)
    doktorlar = Doktor.objects.all()
    if request.method == 'POST':
        DoktorId= request.POST.get('doktor[]')
        Tarih= request.POST.get('RandevuTarihi')
        Saat=request.POST.get('RandevuSaati')
        doktor=Doktor.objects.get(id=DoktorId)
        instance=Randevu.objects.create(RandevuTarihi =Tarih,RandevuSaati=Saat,Hasta=hasta,Doktor=doktor)
        instance.save()
    randevular=Randevu.objects.filter(Hasta=hasta)
    return render(request, 'patientdash.html', {'hasta': hasta,'doktorlar':doktorlar,'randevular':randevular})



def doctordash(request):
    doktor_id = request.session.get('doktor_id')
    # Hasta kimliğine göre hasta nesnesini al
    doktor = Doktor.objects.get(id=doktor_id)
    randevular=Randevu.objects.filter(Doktor=doktor)
    hastalar = [randevu.Hasta for randevu in randevular]


    return render(request,'doctordash.html',{'doktor': doktor,'hastalar':hastalar,'randevular':randevular})

@require_POST
def randevu_sil(request, randevu_id):
    randevu = get_object_or_404(Randevu, id=randevu_id)
    randevu.delete()
    return redirect(reverse('patientdash'))


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


    
