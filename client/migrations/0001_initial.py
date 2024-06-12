# Generated by Django 5.0.6 on 2024-05-20 10:27

import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=255, null=True)),
                ("prenom", models.CharField(max_length=255, null=True)),
                ("email", models.EmailField(max_length=254, null=True)),
                (
                    "tel",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, null=True, region=None
                    ),
                ),
                ("adresse", models.CharField(max_length=255, null=True)),
                (
                    "sexe",
                    models.CharField(
                        choices=[("M", "Masculin"), ("F", "Féminin")],
                        max_length=10,
                        null=True,
                    ),
                ),
                ("age", models.IntegerField(null=True)),
                ("date_creation", models.DateTimeField(auto_now_add=True)),
                (
                    "enregistre_par",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Client",
                "verbose_name_plural": "Clients",
            },
        ),
        migrations.CreateModel(
            name="Facture",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "date_creation_facture",
                    models.DateTimeField(auto_now_add=True, null=True),
                ),
                (
                    "total",
                    models.DecimalField(decimal_places=2, max_digits=1000, null=True),
                ),
                ("date_mise_jour_facture", models.DateTimeField(blank=True, null=True)),
                ("paye", models.BooleanField(default=False)),
                (
                    "type_facture",
                    models.CharField(
                        choices=[
                            ("R", "RECU"),
                            ("P", "FACTURE PROFORMA"),
                            ("F", "FACTURE"),
                        ],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "commentaire",
                    models.TextField(blank=True, max_length=1000, null=True),
                ),
                (
                    "client",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="client.client",
                    ),
                ),
                (
                    "enregistre_par",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Facture",
                "verbose_name_plural": "Factures",
            },
        ),
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("intitule", models.CharField(max_length=255, null=True)),
                ("quantite", models.IntegerField(null=True)),
                (
                    "prix_unitaire",
                    models.DecimalField(decimal_places=2, max_digits=1000, null=True),
                ),
                (
                    "total",
                    models.DecimalField(decimal_places=2, max_digits=1000, null=True),
                ),
                (
                    "facture",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="client.facture",
                    ),
                ),
            ],
            options={
                "verbose_name": "Article",
                "verbose_name_plural": "Articles",
            },
        ),
    ]
