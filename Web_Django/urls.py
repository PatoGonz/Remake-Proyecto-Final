"""Web_Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Registro_lol.views import (index, mostrar_campeones,
                                BuscarCampeones, DetalleCampeon, CrearCampeon, 
                                ActualizarCampeon, BorrarCampeon, SignUp, Login, 
                                Logout, ProfileUpdate, acerca_de, MensajeCreate, MensajeList, MensajeDelete)
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('campeones', mostrar_campeones, name="campeones"),
    # path('campeones/crear', crear_campeon, name="campeones-crear"),
    path('campeones/list', BuscarCampeones.as_view(), name="campeones-list"),
    path('campeones/<pk>/detail', DetalleCampeon.as_view(), name="campeones-detail"),
    path('campeones/create', CrearCampeon.as_view(), name="campeones-create"),
    path('campeones/<pk>/update', ActualizarCampeon.as_view(), name="campeones-update"),
    path('campeones/<pk>/delete', BorrarCampeon.as_view(), name="campeones-delete"),
    path('signup/', SignUp.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', Logout.as_view(), name="logout"),
    path('profile/<pk>/update', ProfileUpdate.as_view(), name="profile-update"),
    path('acerca', acerca_de, name="acerca-de"),
    path('mensaje/create', MensajeCreate.as_view(), name="mensaje-create"),
    path('mensaje/list', MensajeList.as_view(), name="mensaje-list"),
    path('mensaje/<pk>/delete', MensajeDelete.as_view(), name="mensaje-delete"),
    ]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)