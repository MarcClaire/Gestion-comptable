from django.urls import path
from .views import StatistiquesVentesView, StatistiquesDepensesView
urlpatterns = [
	path('graphique-ventes/', StatistiquesVentesView.as_view(), name='graphique_ventes'),
	path('statistiques-depenses/', StatistiquesDepensesView.as_view(), name='graphique_depenses'),

]