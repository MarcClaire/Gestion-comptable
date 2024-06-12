from django.db import models

from django.utils import timezone

# Create your models here.



class Compte(models.Model):
    TYPE_COMPTE_CHOICES = [
        ('Actif', 'Actif'),
        ('Passif', 'Passif'),
        ('Capitaux Propres', 'Capitaux Propres'),
    ]

    nom = models.CharField(max_length=100)
    type_compte = models.CharField(max_length=50, choices=TYPE_COMPTE_CHOICES)
    valeur = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        return f"{self.nom} ({self.type_compte})"

class Transaction(models.Model):
    compte = models.ForeignKey(Compte, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=15, decimal_places=2)
    date = models.DateField(default=timezone.now)
    description = models.TextField()

    def __str__(self):
        return f"{self.description} ({self.montant})"

class Bilan(models.Model):
    date = models.DateField(unique=True)
    actifs_total = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    passifs_total = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    capitaux_propres = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def calculer_actifs_total(self):
        return sum(Transaction.objects.filter(compte__type_compte='Actif').values_list('montant', flat=True))

    def calculer_passifs_total(self):
        return sum(Transaction.objects.filter(compte__type_compte='Passif').values_list('montant', flat=True))

    def calculer_capitaux_propres(self):
        return self.calculer_actifs_total() - self.calculer_passifs_total()

    def get_transactions_by_type(self, type_compte):
        return Transaction.objects.filter(compte__type_compte=type_compte)

    def save(self, *args, **kwargs):
        self.actifs_total = self.calculer_actifs_total()
        self.passifs_total = self.calculer_passifs_total()
        self.capitaux_propres = self.calculer_capitaux_propres()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bilan du {self.date}"
