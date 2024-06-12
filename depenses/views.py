from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Depense, Categorie
from django.views import View
from django.db import transaction
from django.contrib.auth.models import User

# Create your views here.

class DepenseView(View):
    template_name = "depense/liste_depense.html"

    def get(self, request, *args, **kwargs):
        depenses = Depense.objects.all()
        categories = Categorie.objects.all()
        context = {
            'categories': categories,
            'depenses': depenses
        }
        return render(request, self.template_name, context)

def ajouter_categorie(request):
    if request.method == 'POST':
        try:
            intitule = request.POST.get('intitule')
            description = request.POST.get('description')

            Categorie.objects.create(
                intitule=intitule,
                description=description
            )

            messages.success(request, ("Catégorie ajoutée avec succès"))
        except Exception as e:
            messages.error(request, f"Une erreur est survenue : {e}")

        return redirect('mesdepenses')

    return render(request, 'depense/ajouter_categorie.html')

class AjouterDepense(View):
    template_name = "depenses/ajouter_depense.html"

    def get(self, request, *args, **kwargs):
        categories = Categorie.objects.all()
        context = {
            'categories': categories
        }
        return render(request, self.template_name, context)

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        try:
            categorie_id = request.POST.get('categorie')
            motif = request.POST.get('motif')
            date_depense = request.POST.get('date')
            montant = request.POST.get('montant')
            description = request.POST.get('description')

            depense = Depense.objects.create(
                categorie_id=categorie_id,
                motif=motif,
                date_depense=date_depense,
                montant=montant,
                description=description
            )

            messages.success(request, ("Dépense enregistrée avec succès"))
        except Exception as e:
            messages.error(request, f"Une erreur est survenue : {e}")

        return redirect('mesdepenses')

def mise_jourdepense(request, id):
    pass

def supprimer_depense(request, id):
    depense = get_object_or_404(Depense, id=id)
    if request.method == 'POST':
        depense.delete()
        messages.success(request, "Dépense supprimée avec succès")
        return redirect("mesdepenses")
    return render(request, 'depense/confirm_suppress.html', {'depense': depense})





