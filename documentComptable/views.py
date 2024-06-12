from django.shortcuts import render

from django.views.generic import CreateView, UpdateView, DeleteView, ListView, TemplateView

from .models import Bilan

from django.urls import reverse_lazy

from django.utils import timezone

from .models import Compte, Transaction

from .forms import CompteForm, TransactionForm

class CompteListView(ListView):
    model = Compte
    template_name = 'documentComptable/compte_list.html'

class CompteCreateView(CreateView):
    model = Compte
    form_class = CompteForm
    template_name = 'documentComptable/compte_form.html'
    success_url = reverse_lazy('compte_list')

class CompteUpdateView(UpdateView):
    model = Compte
    form_class = CompteForm
    template_name = 'documentComptable/compte_form.html'
    success_url = reverse_lazy('compte_list')

class CompteDeleteView(DeleteView):
    model = Compte
    template_name = 'documentComptable/compte_confirm_delete.html'
    success_url = reverse_lazy('compte_list')

class TransactionListView(ListView):
    model = Transaction
    template_name = 'documentComptable/transaction_list.html'

class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'documentComptable/transaction_form.html'
    success_url = reverse_lazy('transaction_list')

class TransactionUpdateView(UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'documentComptable/transaction_form.html'
    success_url = reverse_lazy('transaction_list')

class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'documentComptable/transaction_confirm_delete.html'
    success_url = reverse_lazy('transaction_list')


# class BilanView(TemplateView):
#     template_name = 'documentComptable/bilan.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         bilan, created = Bilan.objects.get_or_create(date=timezone.now().date())
#         context['bilan'] = bilan
#         return context


class BilanView(TemplateView):
    template_name = 'documentComptable/bilan.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        bilan = Bilan.objects.latest('date')

        context['bilan'] = bilan
        context['actifs_transactions'] = bilan.get_transactions_by_type('Actif')
        context['passifs_transactions'] = bilan.get_transactions_by_type('Passif')
        context['capitaux_transactions'] = bilan.get_transactions_by_type('Capitaux Propres')

        return context

