from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.urls import reverse

from .models import Objekti, EvidencijePrijema, Racuni, StavkeRacuna, Otpremnice, Dobavljaci
from .forms import ObjektiModelForm, EvidencijePrijemaModelForm, RacuniModelForm, StavkeRacunaModelForm, OtpremniceModelForm, DobavljaciModelForm

# Create your views here.
class HomeView(generic.TemplateView):
    template_name = 'approda/home.html'

#--------------------------------

class IndexViewObjekti(generic.ListView):
    template_name = 'approda/objekti_index.html'
    context_object_name = 'objekti'
    def get_queryset(self):
        return Objekti.objects.order_by('pib')

#The render() function takes the request object as its first argument,
#a template name as its second argument and a dictionary as its optional
#third argument. It returns an HttpResponse object of the given template
#rendered with the given context.

class DetailViewObjekti(generic.DetailView):
    model = Objekti
    template_name = 'approda/objekti_details.html'
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Objekti, pib=id_)

#There’s also a get_list_or_404() function, which works just as get_object_or_404() –
#except using filter() instead of get(). It raises Http404 if the list is empty.

class ObjektiCreateView(generic.CreateView):
    template_name = 'approda/objekti_create.html'
    form_class = ObjektiModelForm
    #queryset = Objekti.objects.order_by('pib')
    def form_valid(self,form):
        return super().form_valid(form)
    #def get_success_url(self):
    #    return '/'

class ObjektiUpdateView(generic.UpdateView):
    template_name = 'approda/objekti_create.html'
    form_class = ObjektiModelForm
    def form_valid(self,form):
        return super().form_valid(form)
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Objekti, pib=id_)

class ObjektiDeleteView(generic.DeleteView):
    template_name = 'approda/objekti_delete.html'
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Objekti, pib=id_)
    def get_success_url(self):
        return reverse("objekti_index")

#--------------------------------

class IndexViewEvidencijePrijema(generic.ListView):
    template_name = 'approda/evidencije_prijema_index.html'
    context_object_name = 'evidencije_prijema'
    def get_queryset(self):
        return EvidencijePrijema.objects.order_by('pk_evidencije_prijema')

class DetailViewEvidencijePrijema(generic.DetailView):
    model =  EvidencijePrijema
    template_name = 'approda/evidencije_prijema_details.html'
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(EvidencijePrijema, pk_evidencije_prijema=id_)

class EvidencijePrijemaCreateView(generic.CreateView):
    template_name = 'approda/evidencije_prijema_create.html'
    form_class = EvidencijePrijemaModelForm
    #queryset = EvidencijePrijema.objects.order_by('pib')
    def form_valid(self,form):
        return super().form_valid(form)

class EvidencijePrijemaUpdateView(generic.UpdateView):
    template_name = 'approda/evidencije_prijema_create.html'
    form_class = EvidencijePrijemaModelForm
    def form_valid(self,form):
        return super().form_valid(form)
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(EvidencijePrijema, pk_evidencije_prijema=id_)

class EvidencijePrijemaDeleteView(generic.DeleteView):
    template_name = 'approda/evidencije_prijema_delete.html'
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(EvidencijePrijema, pk_evidencije_prijema=id_)
    def get_success_url(self):
        return reverse("evidencije_prijema_index")

class EvidencijePrijemaIzradaView(generic.DetailView):
    model =  EvidencijePrijema
    template_name = 'approda/evidencije_prijema_izrada.html'
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(EvidencijePrijema, pk_evidencije_prijema=id_)

#--------------------------------

class IndexViewRacuni(generic.ListView):
    template_name = 'approda/racuni_index.html'
    context_object_name = 'racuni'
    def get_queryset(self):
        return Racuni.objects.order_by('racunid')

class DetailViewRacuni(generic.DetailView):
    model =  Racuni
    template_name = 'approda/racuni_details.html'
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Racuni, racunid=id_)

class RacuniCreateView(generic.CreateView):
    template_name = 'approda/racuni_create.html'
    form_class = RacuniModelForm
    #queryset = Racuni.objects.order_by('pib')
    def form_valid(self,form):
        return super().form_valid(form)

class RacuniUpdateView(generic.UpdateView):
    template_name = 'approda/racuni_create.html'
    form_class = RacuniModelForm
    def form_valid(self,form):
        return super().form_valid(form)
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Racuni, racunid=id_)

class RacuniDeleteView(generic.DeleteView):
    template_name = 'approda/racuni_delete.html'
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Racuni, racunid=id_)
    def get_success_url(self):
        return reverse("racuni_index")

#--------------------------------

class IndexViewStavkeRacuna(generic.ListView):
    template_name = 'approda/stavke_racuna_index.html'
    context_object_name = 'stavke_racuna'
    def get_queryset(self):
        return StavkeRacuna.objects.order_by('pk_stavke_racuna')

class DetailViewStavkeRacuna(generic.DetailView):
    model =  StavkeRacuna
    template_name = 'approda/stavke_racuna_details.html'
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(StavkeRacuna, pk_stavke_racuna=id_)

class StavkeRacunaCreateView(generic.CreateView):
    template_name = 'approda/stavke_racuna_create.html'
    form_class = StavkeRacunaModelForm
    #queryset = StavkeRacuna.objects.order_by('pib')
    def form_valid(self,form):
        return super().form_valid(form)

class StavkeRacunaUpdateView(generic.UpdateView):
    template_name = 'approda/stavke_racuna_create.html'
    form_class = StavkeRacunaModelForm
    def form_valid(self,form):
        return super().form_valid(form)
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(StavkeRacuna, pk_stavke_racuna=id_)

class StavkeRacunaDeleteView(generic.DeleteView):
    template_name = 'approda/stavke_racuna_delete.html'
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(StavkeRacuna, pk_stavke_racuna=id_)
    def get_success_url(self):
        return reverse("stavke_racuna_index")

#--------------------------------

class IndexViewOtpremnice(generic.ListView):
    template_name = 'approda/otpremnice_index.html'
    context_object_name = 'otpremnice'
    def get_queryset(self):
        return Otpremnice.objects.order_by('sifra_otpremnice')

class DetailViewOtpremnice(generic.DetailView):
    model =  Otpremnice
    template_name = 'approda/otpremnice_details.html'
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Otpremnice, sifra_otpremnice=id_)

class OtpremniceCreateView(generic.CreateView):
    template_name = 'approda/otpremnice_create.html'
    form_class = OtpremniceModelForm
    #queryset = Otpremnice.objects.order_by('pib')
    def form_valid(self,form):
        return super().form_valid(form)

class OtpremniceUpdateView(generic.UpdateView):
    template_name = 'approda/otpremnice_create.html'
    form_class = OtpremniceModelForm
    def form_valid(self,form):
        return super().form_valid(form)
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Otpremnice, sifra_otpremnice=id_)

class OtpremniceDeleteView(generic.DeleteView):
    template_name = 'approda/otpremnice_delete.html'
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Otpremnice, sifra_otpremnice=id_)
    def get_success_url(self):
        return reverse("otpremnice_index")

#--------------------------------

class IndexViewDobavljaci(generic.ListView):
    template_name = 'approda/dobavljaci_index.html'
    context_object_name = 'dobavljaci'
    def get_queryset(self):
        return Dobavljaci.objects.order_by('sifra_dobavljaca')

class DetailViewDobavljaci(generic.DetailView):
    model =  Dobavljaci
    template_name = 'approda/dobavljaci_details.html'
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Dobavljaci, sifra_dobavljaca=id_)

class DobavljaciCreateView(generic.CreateView):
    template_name = 'approda/dobavljaci_create.html'
    form_class = DobavljaciModelForm
    #queryset = Dobavljaci.objects.order_by('pib')
    def form_valid(self,form):
        return super().form_valid(form)

class DobavljaciUpdateView(generic.UpdateView):
    template_name = 'approda/dobavljaci_create.html'
    form_class = DobavljaciModelForm
    def form_valid(self,form):
        return super().form_valid(form)
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Dobavljaci, sifra_dobavljaca=id_)

class DobavljaciDeleteView(generic.DeleteView):
    template_name = 'approda/dobavljaci_delete.html'
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Dobavljaci, sifra_dobavljaca=id_)
    def get_success_url(self):
        return reverse("dobavljaci_index")

#--------------------------------
