# Generated by Django 5.0.6 on 2024-06-02 20:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("client", "0007_alter_facture_date_creation_facture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="age",
            field=models.CharField(null=True),
        ),
    ]