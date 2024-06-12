from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User 
# Create your models here.


class Client(models.Model):
	nom = models.CharField(max_length=255, null=True)
	prenom =models.CharField(max_length=255, null=True)
	email = models.EmailField(null=True)
	tel = PhoneNumberField(null=True)
	adresse = models.CharField(max_length=255, null=True)
	sexe = models.CharField(max_length=10, choices=[('M', 'Masculin'), ('F', 'Féminin')], null=True)
	age = models.CharField(null=True)
	date_creation = models.DateTimeField(auto_now_add=True)
	enregistre_par = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
	

	class Meta:
		verbose_name = "Client"
		verbose_name_plural = "Clients"


	def __str__(self):
		return f"{self.nom} {self.prenom}"


class Facture(models.Model):

	TYPE_FACTURE =(
		('R', 'RECU'),
		('P', 'FACTURE PROFORMA'),
		('F', 'FACTURE')
	)
	client = models.ForeignKey(Client, on_delete=models.PROTECT, null=True)
	enregistre_par = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
	date_creation_facture = models.DateTimeField(auto_now_add=True)
	total = models.DecimalField(max_digits=1000, decimal_places=2, null=True)
	date_mise_jour_facture = models.DateTimeField(null=True, blank=True)
	paye = models.BooleanField(default=False)
	type_facture = models.CharField(max_length=1, choices=TYPE_FACTURE, null=True)
	commentaire = models.TextField(max_length=1000, null=True, blank=True)

	class Meta:
		verbose_name = 'Facture'
		verbose_name_plural = 'Factures'

	@property
	def get_total(self):
		articles = self.article_set.all()
		total = sum(article.get_total for article in articles)
		return total

	def __str__(self):
		return f"{self.client.nom} {self.date_creation_facture}"

class Article(models.Model):
	facture = models.ForeignKey(Facture, on_delete=models.PROTECT, null=True)
	intitule = models.CharField(max_length=255, null=True)
	quantite = models.IntegerField(null=True)
	prix_unitaire = models.DecimalField(max_digits=1000, decimal_places=2, null=True)
	total= models.DecimalField(max_digits=1000, decimal_places=2, null=True)
	


	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = 'Articles'

	@property
	def get_total(self):
		total = self.quantite * self.prix_unitaire
		return total
	

	def __str__(self):
		return self.intitule

class Fournisseur(models.Model):
	nom = models.CharField(max_length=255, null=True)
	email = models.EmailField(null=True)
	tel = PhoneNumberField(null=True)
	adresse = models.CharField(max_length=255, null=True)
	fournitures = models.CharField(max_length=255, null=True)
	quantite = models.IntegerField(null=True)
	mode_payement = models.BooleanField(default=False)
	date_fourniture = models.DateTimeField(auto_now_add=True, null=True)

	class Meta:
		verbose_name = 'Fournisseur'
		verbose_name_plural = 'Fournisseurs'


	def __str__(self):
		return f"{self.nom}"