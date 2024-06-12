from django.shortcuts import render, redirect


from django.contrib import messages

from .models import *

from .forms import ClientForm, FournisseurForm

from django.views import View

from django.template.loader import get_template

from django.db import transaction

from django.contrib.auth.decorators import login_required

from .utils import pagination, get_facture

from django.utils.translation import gettext as _

from django.contrib.auth.models import User

from django.http import HttpResponse

import pdfkit

import datetime

from .decorators import *

from django.views.generic import TemplateView


class AboutView(TemplateView):
    template_name = 'about.html'


@login_required(login_url='sing_in')
def home(request, *args, **kwargs):
    total_clients = Client.objects.count()
    total_facture = Facture.objects.count()
    return render(request, 'index.html', {'total_clients': total_clients, 'total_facture': total_facture})

#cette fonction permet d'affichier la liste des client

@superuser_required
def liste(request):
    clients = Client.objects.all()
    return render(request,'client/liste.html',{'clients':clients})

#Cette fonctionnalité permet de supprimer des clients
def destroy(request,id):
    client=Client.objects.get(id=id)
    client.delete()
    return redirect("mesclients")


#Cette fonction permet d'ajouter un employé
def ajouterClient(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('mesclients')
            except forms.ValidationError as e:
                # Si une ValidationError est levée, renvoyer le formulaire avec l'erreur
                return render(request, 'client/ajouter_client.html', {'form': form, 'error_message': str(e)}) 
    else:
        form = ClientForm()
    return render(request, 'client/ajouter_client.html', {'form': form})

# #Cette fonction permet de modier les informations d'un client
def updateClient(request, id):
    if request.method== 'POST':
        client= Client.objects.get(pk=id)
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            try:
                form.save()
                return redirect('mesclients')
            except forms.ValidationError as e:
                # Si une ValidationError est levée, renvoyer le formulaire avec l'erreur
                return render(request, 'client/update_client.html', {'form': form, 'error_message': str(e)}) 
    else:
        client = Client.objects.get(pk=id)
        form = ClientForm(instance=client)
    return render(request, 'client/update_client.html', {'form':form} )



def listeFournisseur(request):
    #Affichage de la liste des fournisseurs
    fournisseurs = Fournisseur.objects.all()
    return render(request,'fournisseur/liste.html',{'fournisseurs':fournisseurs})


def ajouterFournisseur(request):
    #Ajout de fournisseur

    if request.method == 'POST':
        form = FournisseurForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('mesfournisseurs')
            except forms.ValidationError as e:
                #renvoie du formulaire si validationError levée
                return render(request, 'fournisseur/ajouter_fournisseur.html', {'form': form, 'error_message': str(e)})
    else:
        form = Fournisseur()
    return render(request, 'fournisseur/ajouter_fournisseur.html', {'form': form})



def updateFournisseur(request, id):
    # Modificationdes information d'un fournisseur

    if request.method== 'POST':
        fournisseur= Fournisseur.objects.get(pk=id)
        form = FournisseurForm(request.POST, instance=client)
        if form.is_valid():
            try:
                form.save()
                return redirect('mesfournisseurs')
            except forms.ValidationError as e:
                # Renvoyer le formulaire avec l'erreur si ValidationError levé
                return render(request, 'fournisseur/update_founisseur.html', {'form': form, 'error_message': str(e)})
    else:
        fournisseur = Fournisseur.objects.get(pk=id)
        form = FournisseurForm(instance=fournisseur)
    return render(request, 'fournisseur', {'form':form})


def destroyFournisseur(request,id):
    #Suppression de fournisseurs
    
    fournisseur=Fournisseur.objects.get(id=id)
    fournisseur.delete()
    return redirect("mesfournisseurs")
#////////

class FournisseurView(LoginRequiredSuperuserMixim, View):
    """ Main view """

    templates_name = 'fournisseur/liste.html'

    fournisseurs = Fournisseur.objects.all().order_by('date_fourniture')

    context = {
        'fournisseurs': fournisseurs
    }

    def get(self, request, *args, **kwags):

        items = pagination(request, self.fournisseurs)

        self.context['fournisseurs'] = items

        return render(request, self.templates_name, self.context)


    def post(self, request, *args, **kwagrs):

        # modifier fournisseur

        if request.POST.get('id_modified'):

            paye = request.POST.get('modified')

            try: 

                fourni = Fournisseur.objects.get(id=request.POST.get('id_modified'))
 
                if mode_payement == 'True':

                    fourni.mode_payement = True

                else:

                    fourni.mode_payement = False 

                fourni.save() 

                messages.success(request,  _("Change made successfully.")) 

            except Exception as e:   

                messages.error(request, f"Sorry, the following error has occured {e}.")      

        # suprimer facture    

        if request.POST.get('id_supprimer'):

            try:

                fourni = Facture.objects.get(pk=request.POST.get('id_supprimer'))

                fourni.delete()

                messages.success(request, _("The deletion was successful."))   

            except Exception as e:

                messages.error(request, f"Sorry, the following error has occured {e}.")      

        items = pagination(request, self.factures)

        self.context['fournisseurs'] = items

        return render(request, self.templates_name, self.context) 

#///////////////////////////////////////////////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////

# Create your views here.

class HomeView(LoginRequiredSuperuserMixim, View):
    """ Main view """

    templates_name = 'facture/liste_facture.html'

    factures = Facture.objects.select_related('client', 'enregistre_par').all().order_by('date_creation_facture')

    context = {
        'factures': factures
    }

    def get(self, request, *args, **kwags):

        items = pagination(request, self.factures)

        self.context['factures'] = items

        return render(request, self.templates_name, self.context)


    def post(self, request, *args, **kwagrs):

        # modifier facture

        if request.POST.get('id_modified'):

            paye = request.POST.get('modified')

            try: 

                obj = Facture.objects.get(id=request.POST.get('id_modified'))
 
                if paye == 'True':

                    obj.paye = True

                else:

                    obj.paye = False 

                obj.save() 

                messages.success(request,  _("Change made successfully.")) 

            except Exception as e:   

                messages.error(request, f"Sorry, the following error has occured {e}.")      

        # suprimer facture    

        if request.POST.get('id_supprimer'):

            try:

                obj = Facture.objects.get(pk=request.POST.get('id_supprimer'))

                obj.delete()

                messages.success(request, _("The deletion was successful."))   

            except Exception as e:

                messages.error(request, f"Sorry, the following error has occured {e}.")      

        items = pagination(request, self.factures)

        self.context['factures'] = items

        return render(request, self.templates_name, self.context)    



class AjouterFactureView(View, LoginRequiredSuperuserMixim):
    """ add a new invoice view """

    template_name = 'facture/ajouter_facture.html'

    clients = Client.objects.select_related('enregistre_par').all()

    context = {
        'clients': clients
    }

    def get(self, request, *args, **kwargs):
        return  render(request, self.template_name, self.context)

    @transaction.atomic()
    def post(self, request, *args, **kwargs):
        print(request.POST)
        
        items = []

        try: 

            client = request.POST.get('client')

            type_facture = request.POST.get('type_facture')

            articles = request.POST.getlist('article')

            qties = request.POST.getlist('qty')

            units = request.POST.getlist('unit')

            total_a = request.POST.getlist('total-a')

            total = request.POST.get('total')

            comment = request.POST.get('comment')

            facture_object = {
                'client_id': client,
                'enregistre_par': request.user,
                'date_creation_facture': date_creation_facture,
                'total': total,
                'type_facture': type_facture,
                'commentaire': comment
            }

            facture = Facture.objects.create(**facture_object)

            for index, article in enumerate(articles):

                data = Article(
                    facture_id = facture.id,
                    intitule = article,
                    quantite=qties[index],
                    prix_unitaire = units[index],
                    total = total_a[index],
                )

                items.append(data)

            created = Article.objects.bulk_create(items)   

            if created:
                messages.success(request, "Facture enregistré avec succès") 
            else:
                messages.error(request, "Sorry, please try again the sent data is corrupt.")    

        except Exception as e:
            print(e)
            messages.error(request, f"Sorry the following error has occured {e}.")   

        return  render(request, self.template_name, self.context)

class VisualisationFacture(View, LoginRequiredSuperuserMixim):
    template_name = "facture/detail_facture.html"
  
    def get(self, request, *args, **kwargs):

        id = kwargs.get('id')

        context = get_facture(id)

        return render(request, self.template_name, context)


def genere_facture_pdf(request, *args, **kwargs):
    """ generate pdf file from html file """

    id = kwargs.get('id')

    obj = Facture .objects.get(id=id)

    context = get_facture(id)

    context['date'] = datetime.datetime.today()

    # get html file
    template_html = get_template('facture/facture-pdf.html')

    # render html with context variables

    html = template_html.render(context)

    # option du format pdf 

    options = {
        'page-size': 'Letter',
        'encoding': 'UTF-8',
        "enable-local-file-access": ""
    }

    # Path to the wkhtmltopdf executable
    path_wkhtmltopdf = r'C:\Program Files (x86)\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    # generate pdf 

    pdf = pdfkit.from_string(html, False, options)

    response = HttpResponse(pdf, content_type='application/pdf')
    
    filename = f"{obj.client.nom}-{obj.date_creation_facture}.pdf"
    
    response['Content-Disposition'] = f'attachment; filename="{filename}"'
    
    return response