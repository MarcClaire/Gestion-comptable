from django.contrib import admin
from .models import *


from django.utils.translation import gettext_lazy as _
# Register your models here.


class AdminClient(admin.ModelAdmin):
	list_display = ('nom', 'prenom', 'email', 'tel', 'adresse', 'sexe', 'age', 'date_creation', 'enregistre_par')

class AdminFacture(admin.ModelAdmin):
	list_display = ('client', 'enregistre_par', 'date_creation_facture', 'total','date_mise_jour_facture', 'paye', 'type_facture', 'commentaire')

class AdminArticle(admin.ModelAdmin):
	list_display = ( 'facture', 'intitule', 'quantite', 'prix_unitaire', 'total' )

class AdminFournisseur(admin.ModelAdmin):
	list_display = ( 'nom', 'email', 'tel', 'adresse', 'fournitures', 'quantite', 'mode_payement', 'date_fourniture' )

admin.site.register(Client, AdminClient)
admin.site.register(Facture, AdminFacture)
admin.site.register(Article, AdminArticle)
admin.site.register(Fournisseur, AdminFournisseur)

admin.site.site_title = _("Application de gestion Comptable")
admin.site.site_header = _("Administration Comptable")
admin.site.index_title = _("Administration comptable")