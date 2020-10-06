from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name='home_view'),
    path('objekti/',views.IndexViewObjekti.as_view(), name='objekti_index'),
    path('objekti/<int:id>/', views.DetailViewObjekti.as_view(), name='objekti_details'),
    path('objekti/create/', views.ObjektiCreateView.as_view(), name='objekti_create'),
    path('objekti/<int:id>/update/', views.ObjektiUpdateView.as_view(), name='objekti_update'),
    path('objekti/<int:id>/delete/', views.ObjektiDeleteView.as_view(), name='objekti_delete'),

    path('evidencije_prijema/',views.IndexViewEvidencijePrijema.as_view(), name='evidencije_prijema_index'),
    path('evidencije_prijema/<int:id>/', views.DetailViewEvidencijePrijema.as_view(), name='evidencije_prijema_details'),
    path('evidencije_prijema/create/', views.EvidencijePrijemaCreateView.as_view(), name='evidencije_prijema_create'),
    path('evidencije_prijema/<int:id>/update/', views.EvidencijePrijemaUpdateView.as_view(), name='evidencije_prijema_update'),
    path('evidencije_prijema/<int:id>/delete/', views.EvidencijePrijemaDeleteView.as_view(), name='evidencije_prijema_delete'),
    path('evidencije_prijema/<int:id>/izrada/', views.EvidencijePrijemaIzradaView.as_view(), name='evidencije_prijema_izrada'),

    path('racuni/',views.IndexViewRacuni.as_view(), name='racuni_index'),
    path('racuni/<int:id>/', views.DetailViewRacuni.as_view(), name='racuni_details'),
    path('racuni/create/', views.RacuniCreateView.as_view(), name='racuni_create'),
    path('racuni/<int:id>/update/', views.RacuniUpdateView.as_view(), name='racuni_update'),
    path('racuni/<int:id>/delete/', views.RacuniDeleteView.as_view(), name='racuni_delete'),

    path('stavke_racuna/',views.IndexViewStavkeRacuna.as_view(), name='stavke_racuna_index'),
    path('stavke_racuna/<int:id>/', views.DetailViewStavkeRacuna.as_view(), name='stavke_racuna_details'),
    path('stavke_racuna/create/', views.StavkeRacunaCreateView.as_view(), name='stavke_racuna_create'),
    path('stavke_racuna/<int:id>/update/', views.StavkeRacunaUpdateView.as_view(), name='stavke_racuna_update'),
    path('stavke_racuna/<int:id>/delete/', views.StavkeRacunaDeleteView.as_view(), name='stavke_racuna_delete'),

    path('otpremnice/',views.IndexViewOtpremnice.as_view(), name='otpremnice_index'),
    path('otpremnice/<int:id>/', views.DetailViewOtpremnice.as_view(), name='otpremnice_details'),
    path('otpremnice/create/', views.OtpremniceCreateView.as_view(), name='otpremnice_create'),
    path('otpremnice/<int:id>/update/', views.OtpremniceUpdateView.as_view(), name='otpremnice_update'),
    path('otpremnice/<int:id>/delete/', views.OtpremniceDeleteView.as_view(), name='otpremnice_delete'),

    path('dobavljaci/',views.IndexViewDobavljaci.as_view(), name='dobavljaci_index'),
    path('dobavljaci/<int:id>/', views.DetailViewDobavljaci.as_view(), name='dobavljaci_details'),
    path('dobavljaci/create/', views.DobavljaciCreateView.as_view(), name='dobavljaci_create'),
    path('dobavljaci/<int:id>/update/', views.DobavljaciUpdateView.as_view(), name='dobavljaci_update'),
    path('dobavljaci/<int:id>/delete/', views.DobavljaciDeleteView.as_view(), name='dobavljaci_delete'),
]
