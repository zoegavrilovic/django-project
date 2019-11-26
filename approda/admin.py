from django.contrib import admin

# Register your models here.
from .models import Kupci, Racuni, Artikli, StavkeRacuna, Objekti, Dobavljaci, Otpremnice, EvidencijePrijema

admin.site.register(Kupci)
admin.site.register(Racuni)
admin.site.register(Artikli)
admin.site.register(StavkeRacuna)
admin.site.register(Objekti)
admin.site.register(Dobavljaci)
admin.site.register(Otpremnice)
admin.site.register(EvidencijePrijema)
