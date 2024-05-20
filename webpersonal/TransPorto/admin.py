from django.contrib import admin
from .models import Usuarios, CooperativaTransporte, Informes, Rutas, PersonalAdministrativo, UnidadTransporte, Conductores, HistorialTransacciones, RegistroAcceso, Tarjeta

admin.site.register(Usuarios)
admin.site.register(CooperativaTransporte)
admin.site.register(Informes)
admin.site.register(Rutas)
admin.site.register(PersonalAdministrativo)
admin.site.register(UnidadTransporte)
admin.site.register(Conductores)
admin.site.register(HistorialTransacciones)
admin.site.register(RegistroAcceso)
admin.site.register(Tarjeta)
