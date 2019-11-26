from django import forms
from .models import Objekti, EvidencijePrijema, Racuni, StavkeRacuna, Otpremnice, Dobavljaci

class ObjektiModelForm(forms.ModelForm):
    class Meta:
        model = Objekti
        fields = [
            'pib',
            'naziv',
            'adresa',
            'grad',
            'broj_telefona',
        ]

class EvidencijePrijemaModelForm(forms.ModelForm):
    class Meta:
        model = EvidencijePrijema
        fields = [
            'kolicina',
            'broj_kalkulacija',
            'sifra_artikla',
            'pib',
            'sifra_otpremnice',
            'naziv_objekta',
        ]

class RacuniModelForm(forms.ModelForm):
    class Meta:
        model = Racuni
        fields = [
            'racunid',
            'datum',
            'vreme',
            'ukupno',
            'kartica',
            'jmbg',
        ]

class StavkeRacunaModelForm(forms.ModelForm):
    class Meta:
        model = StavkeRacuna
        fields = [
            'kolicina',
            'sifra_artikla',
            'racunid',
        ]

class OtpremniceModelForm(forms.ModelForm):
    class Meta:
        model = Otpremnice
        fields = [
            'sifra_otpremnice',
            'datum_otpreme',
            'sifra_dobavljaca',
        ]

class DobavljaciModelForm(forms.ModelForm):
    class Meta:
        model = Dobavljaci
        fields = [
            'sifra_dobavljaca',
            'naziv',
        ]
