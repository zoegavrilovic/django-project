from django.db import models
import datetime
from django.urls import reverse
# Create your models here.
#each model is represented by a class that subclasses django.db.models.Model

class Kupci(models.Model):
    jmbg = models.BigIntegerField(primary_key=True)
    ime = models.CharField(max_length=15,blank=True,null=True)
    prezime = models.CharField(max_length=20,blank=True,null=True)
    kartica = models.BigIntegerField(blank=True,null=True)
    class Meta:
        db_table = 'kupci'
    def __str__(self):
        return "%s, %s, %s, %s" % (self.jmbg, self.ime, self.prezime, self.kartica)

class Racuni(models.Model):
    racunid = models.BigIntegerField(primary_key=True)
    datum = models.DateField()
    vreme = models.CharField(max_length=8)
    ukupno = models.BigIntegerField(null=True)
    kartica = models.BigIntegerField(blank=True,null=True)
    jmbg = models.ForeignKey(Kupci, on_delete=models.CASCADE, db_column='jmbg')
    class Meta:
        db_table = 'racuni'
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s" % (self.racunid, self.datum, self.vreme, self.ukupno, self.kartica, self.jmbg)
    def get_absolute_url(self):
        return reverse("racuni_details", kwargs={"id":self.racunid})

class Artikli(models.Model):
    sifra_artikla = models.BigIntegerField(primary_key=True)
    naziv = models.CharField(max_length=15)
    cena = models.IntegerField()
    jedinica_mere = models.CharField(max_length=8)
    rok_trajanja = models.DateField()
    class Meta:
        db_table = 'artikli'
    def __str__(self):
        return "%s, %s, %s, %s, %s" % (self.sifra_artikla, self.naziv, self.cena, self.jedinica_mere, self.rok_trajanja)

class StavkeRacuna(models.Model):
    # id = models.AutoField(primary_key=True)
    kolicina = models.IntegerField()
    sifra_artikla = models.ForeignKey(Artikli, on_delete=models.CASCADE, db_column='sifra_artikla')
    racunid = models.ForeignKey(Racuni, on_delete=models.CASCADE, db_column='racunid')
    class Meta:
        managed = True
        db_table = 'stavke_racuna'
        unique_together = (('sifra_artikla', 'racunid'),)
    def __str__(self):
        return "%s, %s, %s" % (self.kolicina, self.sifra_artikla, self.racunid)
    def get_absolute_url(self):
        return reverse("stavke_racuna_details", kwargs={"id":self.ID})

class Objekti(models.Model):
    pib = models.BigIntegerField(primary_key=True)
    naziv = models.CharField(max_length=20)
    adresa = models.CharField(max_length=40)
    grad = models.CharField(max_length=15)
    broj_telefona = models.IntegerField(blank=True, null=True)
    class Meta:
        db_table = 'objekti'
    def __str__(self):
        return "%s, %s, %s, %s, %s" % (self.pib, self.naziv, self.adresa, self.grad, self.broj_telefona)
    def get_absolute_url(self):
        return reverse("objekti_details", kwargs={"id":self.pib})

class Dobavljaci(models.Model):
    sifra_dobavljaca = models.BigIntegerField(primary_key=True)
    naziv = models.CharField(max_length=20)
    class Meta:
        db_table = 'dobavljaci'
    def __str__(self):
        return "%s, %s" % (self.sifra_dobavljaca, self.naziv)
    def get_absolute_url(self):
        return reverse("dobavljaci_details", kwargs={"id":self.sifra_dobavljaca})

class Otpremnice(models.Model):
    sifra_otpremnice = models.BigIntegerField(primary_key=True)
    datum_otpreme = models.DateField()
    sifra_dobavljaca = models.ForeignKey(Dobavljaci, on_delete=models.CASCADE, db_column='sifra_dobavljaca')
    class Meta:
        db_table = 'otpremnice'
        unique_together = (('sifra_otpremnice', 'sifra_dobavljaca'),)
    def __str__(self):
        return "%s, %s, %s" % (self.sifra_otpremnice, self.datum_otpreme, self.sifra_dobavljaca)
    def get_absolute_url(self):
        return reverse("otpremnice_details", kwargs={"id":self.sifra_otpremnice})

class EvidencijePrijema(models.Model):
    # id = models.AutoField(primary_key=True)
    kolicina = models.IntegerField()
    broj_kalkulacija = models.IntegerField(blank=True, null=True)
    sifra_artikla = models.ForeignKey(Artikli, on_delete=models.CASCADE, db_column='sifra_artikla')
    pib = models.ForeignKey(Objekti, on_delete=models.CASCADE, db_column='pib')
    sifra_otpremnice = models.ForeignKey(Otpremnice, on_delete=models.CASCADE, db_column='sifra_otpremnice')
    naziv_objekta = models.CharField(max_length=20, null=True)
    class Meta:
        managed = True
        db_table = 'evidencije_prijema'
        unique_together = (('sifra_artikla', 'pib', 'sifra_otpremnice'),)
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s" % (self.kolicina, self.broj_kalkulacija, self.sifra_artikla, self.pib, self.sifra_otpremnice, self.naziv_objekta)
    def get_absolute_url(self):
        return reverse("evidencije_prijema_details", kwargs={"id":self.ID})
#That small bit of model code gives Django a lot of information. With it, Django is able to:

#Create a database schema (CREATE TABLE statements) for this app.
#Create a Python database-access API for accessing Question and Choice objects.

#To include the app in our project, we need to add a reference to its configuration
#class in the INSTALLED_APPS setting. The PollsConfig class is in the polls/apps.py file,
#so its dotted path is 'polls.apps.PollsConfig'
