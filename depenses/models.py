from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Categorie(models.Model):
	'''catégorie pour regrouper les différente dépenses'''
	
	intitule = models.CharField(max_length=255, null=True)
	description = models.TextField(null=True)
	total= models.DecimalField(max_digits=1000, decimal_places=2, null=True)

	class Meta:
		verbose_name = "Categorie"
		verbose_name_plural = "Categories"

	def __str__(self):
		return f"{self.intitule}"

	@property
	def get_total(self):
		depenses = self.depense_set.all()
		total = sum(depense.montant for depense in depenses)
		return total

class Depense(models.Model):
	'''Les dépenses efectuer par l'entreprise'''
	categorie = models.ForeignKey(Categorie, on_delete=models.PROTECT, null=True)
	enregistre_par = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
	motif = models.CharField(max_length=255)
	date_depense = models.DateTimeField(auto_now_add=True)
	date_mise_jour_depense = models.DateTimeField(null=True, blank=True)
	montant = models.DecimalField(max_digits=1000, decimal_places=2, null=True)
	description = models.TextField(null=True)

	class Meta:
		verbose_name = "Depense"
		verbose_name_plural = "Depenses"

	def __str__(self):
		return f"{self.categorie.intitule}"




