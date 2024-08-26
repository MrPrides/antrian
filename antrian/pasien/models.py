from django.db import models

# Create your models here.
class Pasien (models.Model):
    no_mr = models.CharField(max_length=20, unique=True)
    nama= models.CharField(max_length=50)
    tgl_lahir=models.DateField()
    alamat=models.TextField()
    
    def __str__(self):
        return self.nama
    
    
class Dokter(models.Model):
    dokter_spesialis=models.CharField(max_length=50)
    nama_dokter=models.CharField(max_length=50)
    jadwal_praktek=models.CharField(max_length=200)
    
    def __str__(self):
        return self.nama_dokter
    
class Pendaftaran(models.Model):
    pasien = models.ForeignKey(Pasien, on_delete=models.CASCADE)
    dokter = models.ForeignKey(Dokter, on_delete=models.CASCADE)
    nomor_antrian = models.IntegerField()
    tanggal_berobat = models.DateField()
    waktu_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Pendaftaran {self.pasien.nama} - {self.dokter.nama_dokter}'