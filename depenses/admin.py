from django.contrib import admin

from .models import *

# Register your models here.

class AdminCategorie(admin.ModelAdmin):
	list_display = ('intitule', 'description', 'total')


class AdminDepense(admin.ModelAdmin):
	list_display = ('categorie', 'enregistre_par', 'motif', 'date_depense', 'date_mise_jour_depense', 'montant', 'description')


admin.site.register(Categorie, AdminCategorie),
admin.site.register(Depense, AdminDepense)