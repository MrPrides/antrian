from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import Pasien,Dokter,Pendaftaran
from .forms import PendaftaranForm

# Create your views here.
def pasien_list(request):
    pasien_list=Pasien.objects.all()
    
    return render(request,'pasien_list.html',{'pasien_list': pasien_list})

def pasien_detail(request, pk):
    pasien = get_object_or_404(Pasien, pk=pk)
    dokter_list = Dokter.objects.all()
    
    if request.method == 'POST':
        form = PendaftaranForm(request.POST)
        
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.pasien = pasien
            
            
            existing_appointment = Pendaftaran.objects.filter(
                pasien=pasien,
                dokter=appointment.dokter,
                tanggal_berobat=appointment.tanggal_berobat
            ).exists()
            
            if existing_appointment:
                
                messages.error(request, 'Anda sudah terdaftar pada tanggal ini.')
                return render(request, 'pasien_detail.html', {
                    'pasien': pasien,
                    'dokter_list': dokter_list,
                    'form': form
                })
            else:
                
                today_appointments = Pendaftaran.objects.filter(
                    dokter=appointment.dokter,
                    tanggal_berobat=appointment.tanggal_berobat
                ).count()
                appointment.nomor_antrian = today_appointments + 1
                
                appointment.save()
                messages.success(request, 'Pendaftaran berhasil dilakukan!')
                # return redirect('pendaftaran_list')  # Redirect after saving
        else:
            
            messages.error(request, 'Terjadi kesalahan dalam pendaftaran. Silakan coba lagi.')
            print("Form errors:", form.errors)
    else:
              form = PendaftaranForm()

    context = {
        'pasien': pasien,
        'dokter_list': dokter_list,
        'form': form,
        
    }
    return render(request, 'pasien_detail.html', context)
    
  
        
def pendaftaran_list(request):
    # Get the 'dokter_spesialis' query parameter from the request
    dokter_spesialis = request.GET.get('dokter_spesialis', None)

    if dokter_spesialis:
        # Filter pendaftaran based on dokter_spesialis
        pendaftaran = Pendaftaran.objects.filter(dokter__dokter_spesialis=dokter_spesialis)
    else:
        # Get all pendaftaran if no filter is applied
        pendaftaran = Pendaftaran.objects.all()

    # Get the unique dokter spesialis values for filtering options
    spesialis_list = Dokter.objects.values_list('dokter_spesialis', flat=True).distinct()

    context = {
        'pendaftaran': pendaftaran,
        'spesialis_list': spesialis_list,
    }
    return render(request, 'pendaftaran_list.html', context)