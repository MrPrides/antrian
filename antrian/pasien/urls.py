from django.urls import path,include
from pasien import views

urlpatterns = [
    path('pasien/', views.pasien_list, name='pasien_list'),
    path('pasien/<int:pk>/',views.pasien_detail, name='pasien_detail'),
    # path('pasien/<int:pk>/add/',views.pendaftaran, name='pendaftaran'),
    path('pendaftaran_list/',views.pendaftaran_list, name='pendaftaran_list')
    
    
]
