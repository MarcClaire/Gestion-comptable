from django import forms
from .models import *
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class DateInput(forms.DateInput):
    input_type = 'date'
    
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    def clean_nom(self):
        nom = self.cleaned_data['nom']
        if any(char.isdigit() for char in nom):
            raise ValidationError("Le nom ne peut pas contenir des chiffres.")
        return nom

    def clean_prenom(self):
        prenom = self.cleaned_data['prenom']
        if any(char.isdigit() for char in prenom):
            raise ValidationError("Les prénoms ne peuvent pas contenir des chiffres.")
        return prenom

    nom = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    prenom = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    tel = PhoneNumberField(
        region='BF', 
        widget=PhoneNumberPrefixWidget(initial="BF", attrs={'class': 'form-control', 'placeholder': 'Numéro de téléphone'})
    )
    adresse = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    sexe = forms.ChoiceField(
        choices=[('M', 'Masculin'), ('F', 'Féminin')],
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    age = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    date_creation =forms.DateField(
        widget=DateInput(
            attrs={'class': 'form-control'}), 
        input_formats=['%Y-%m-%d'],
        required=True,
    )
    enregistre_par = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        required=True,
    )



# Partie fournisseur
class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = {'nom', 'email', 'tel', 'adresse', 'fournitures', 'quantite', 'date_fournoture'}

    def clean_nom(self):
        nom = self.cleaned_data['nom']
        if any(char.isdigit() for char in nom):
            raise ValidationError("Chiffre non pris en compte dans le nom !")
        return nom
    nom = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    tel = PhoneNumberField(
        region='BF',
        widget=PhoneNumberPrefixWidget(initial='BF', attrs={'class': 'form-control', 'placeholder': 'Entrez votre numero de telephone'})
    )
    adresse = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    fournitures = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    quantite= forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control'})
        )
    date_fournoture=forms.DateField(
        widget=DateInput(
            attrs={'class': 'form-control'}), 
        input_formats=['%Y-%m-%d'],
        required=True,
        )