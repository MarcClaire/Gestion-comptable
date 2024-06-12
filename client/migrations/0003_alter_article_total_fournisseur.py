# Generated by Django 5.0.6 on 2024-05-28 08:07

import django.db.models.deletion
import phonenumber_field.modelfields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("client", "0002_alter_article_total"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="total",
            field=models.DecimalField(decimal_places=2, max_digits=1000, null=True),
        ),
        migrations.CreateModel(
            name="Fournisseur",
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
                ("email", models.EmailField(max_length=254, null=True)),
                (
                    "tel",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, null=True, region=None
                    ),
                ),
                ("adresse", models.CharField(max_length=255, null=True)),
                ("fournitures", models.CharField(max_length=255, null=True)),
                ("mode_payement", models.BooleanField(default=False)),
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
                "verbose_name": "Fournisseur",
                "verbose_name_plural": "Fournisseurs",
            },
        ),
    ]
