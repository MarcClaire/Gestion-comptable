from django.urls import path
from . import views

urlpatterns = [
    path('depense/',views.DepenseView.as_view(), name='mesdepenses'),
    path('ajouter-dep', views.AjouterDepense.as_view(), name='addDepense'),
    #path('mise-jr-dep/<int:id>',views.mise_jourdepense, name='updateDepense'),
    path('sup-dep/<int:id>/',views.supprimer_depense, name='destroyDepense'),
    path('ajouter-cat/', views.ajouter_categorie, name='addCategorie'),

    
]