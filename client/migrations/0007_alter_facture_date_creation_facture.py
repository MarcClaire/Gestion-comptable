# Generated by Django 5.0.6 on 2024-05-29 21:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("client", "0006_fournisseur_date_fourniture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="facture",
            name="date_creation_facture",
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
    ]
