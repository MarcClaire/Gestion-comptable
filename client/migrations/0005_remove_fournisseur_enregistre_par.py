# Generated by Django 5.0.6 on 2024-05-28 09:06

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("client", "0004_fournisseur_quantite_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="fournisseur",
            name="enregistre_par",
        ),
    ]