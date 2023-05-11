from typing import Any, Optional
from django.db.models.query import QuerySet
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from Registro_lol.models import Campeon, Profile, Mensaje
from Registro_lol.forms import CampeonForm
from django.contrib.auth.decorators import *
from django.views.generic import *
from Registro_lol.forms import *
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

def index(request):
      campeones = Campeon.objects.all()
      context = {
      "campeones": campeones,
       "form": CampeonForm()
      
      }
      return render(request, "Registro_lol/index.html", context)


def mostrar_campeones(request):
      campeones = Campeon.objects.all()
      context = {
      "campeones": campeones,
       "form": CampeonForm()
      
      }
      return render(request, "Registro_lol/campeones.html", context)

class BuscarCampeones(ListView):
      model = Campeon
      context_object_name = "campeones"

      def get_queryset(self):
            f = BuscarCampeonesForm(self.request.GET)
            if f.is_valid():
                  return Campeon.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all()
            
            return Campeon.objects.none()

class DetalleCampeon(DetailView):
      model = Campeon

class CrearCampeon(LoginRequiredMixin, CreateView):
      model = Campeon
      success_url = reverse_lazy("index")
      fields = ['nombre','descripcion','dificultad', 'imagen']

      def form_valid(self, form):
            form.instance.publisher = self.request.user
            return super().form_valid(form)

class ActualizarCampeon(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
      model = Campeon
      success_url = reverse_lazy("campeones-list")
      fields = '__all__'

      def test_func(self):
            user_id = self.request.user.id
            campeon_id = self.kwargs.get('pk')

            return Campeon.objects.filter(publisher=user_id, id=campeon_id).exists()

      def handle_no_permission(self):
            return render(self.request, "Registro_lol/not_found.html")

class BorrarCampeon(LoginRequiredMixin,DeleteView):
      model = Campeon
      success_url = reverse_lazy("campeones-list")
       
class SignUp(CreateView):
      form_class = UserCreationForm
      template_name = 'registration/signup.html'
      success_url = reverse_lazy('index')

class Login(LoginView):
      next_page = reverse_lazy('index')

class Logout(LogoutView):
      template_name = 'registration/logout.html'

class ProfileUpdate(UpdateView):
      model = Profile
      fields = '__all__'

def acerca_de(request):
      return render(request, "Registro_lol/acerca_de_mi.html")

class MensajeCreate(CreateView):
      model = Mensaje
      fields = '__all__'
      success_url = reverse_lazy("index")

class MensajeList(LoginRequiredMixin,ListView):
      model = Mensaje
      context_object_name = "mensajes"

      def get_queryset(self):
            return Mensaje.objects.filter(destinatario=self.request.user.id).all()
      
class MensajeDelete(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
      model = Mensaje
      success_url = reverse_lazy("mensaje-list")

      def test_func(self):
            user_id = self.request.user.id
            mensaje_id = self.kwargs.get('pk')

            return Mensaje.objects.filter(destinatario=user_id).exists()

      def handle_no_permission(self):
            return render(self.request, "Registro_lol/not_found.html")