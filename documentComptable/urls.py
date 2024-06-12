from django.urls import path
from .views import (
    CompteListView, CompteCreateView, CompteUpdateView, CompteDeleteView,
    TransactionListView, TransactionCreateView, TransactionUpdateView, TransactionDeleteView, BilanView)
urlpatterns = [

	path('comptes/', CompteListView.as_view(), name='compte_list'),
    path('comptes/ajouter/', CompteCreateView.as_view(), name='compte_create'),
    path('comptes/modifier/<int:pk>/', CompteUpdateView.as_view(), name='compte_update'),
    path('comptes/supprimer/<int:pk>/', CompteDeleteView.as_view(), name='compte_delete'),

    path('transactions/', TransactionListView.as_view(), name='transaction_list'),
    path('transactions/ajouter/', TransactionCreateView.as_view(), name='transaction_create'),
    path('transactions/modifier/<int:pk>/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('transactions/supprimer/<int:pk>/', TransactionDeleteView.as_view(), name='transaction_delete'),

	path('bilan/', BilanView.as_view(), name='bilan'),
	
]

