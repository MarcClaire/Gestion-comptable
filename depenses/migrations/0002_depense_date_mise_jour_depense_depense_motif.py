# Generated by Django 5.0.6 on 2024-05-31 13:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("depenses", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="depense",
            name="date_mise_jour_depense",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="depense",
            name="motif",
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
