from django import forms
from .models import Compte, Transaction


class DateInput(forms.DateInput):
    input_type = 'date'

class CompteForm(forms.ModelForm):
    class Meta:
        model = Compte
        fields = ['nom', 'type_compte', 'valeur']

    nom = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
        )
    type_compte = forms.ChoiceField(
        choices=[('Actif', 'Actif'), ('Passif', 'Passif'), ('Capitaux Propres', 'Capitaux Propres')],
        widget=forms.Select(attrs={'class': 'form-control'})
        )
    valeur = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
        )


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['compte', 'montant', 'date', 'description']

    compte = forms.ModelChoiceField(
        queryset=Compte.objects.all(), 
        widget=forms.Select(attrs={'class': 'form-control'})
        )

    montant = forms.DecimalField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
        )
    date = forms.DateField(
        widget=DateInput(
            attrs={'class': 'form-control'}), 
        input_formats=['%Y-%m-%d'],
        )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={'class': 'form-control'}),
        )