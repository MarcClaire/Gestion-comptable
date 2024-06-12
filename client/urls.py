from django.urls import path
from . import views
from .views import AboutView

urlpatterns = [
    path('',views.home, name='home'),

    path('about/', AboutView.as_view(), name='about'),

    path('clt/',views.liste, name= 'mesclients'),
    path("destroy-clt/<int:id>",views.destroy,name='destroyClient'),
    path('ajouter-clt/', views.ajouterClient, name='addClient'),
    path('update-clt/<int:id>',views.updateClient, name='updateclient'),
    
    path('fourni/', views.listeFournisseur, name='mesfournisseurs'),
    path('ajouter-fourni', views.ajouterFournisseur, name='addFournisseur'),
    path('update-fourni/<int:id>',views.updateFournisseur, name= 'updatefournisseur'),
    path("destroy/<int:id>",views.destroyFournisseur,name='destroyFournisseur'),
    path('fournitures', views.FournisseurView.as_view(), name='supupdateFourn'),
    
    path('ajouter-fact', views.HomeView.as_view(), name='mesfactures'),
    path('liste-fact', views.AjouterFactureView.as_view(), name='addfacture'),
    path('voir-facture/<int:id>',views.VisualisationFacture.as_view(),name='detaiFacture'),
    path('generer-facture/<int:id>',views.genere_facture_pdf ,name='genererFacture'),

]



