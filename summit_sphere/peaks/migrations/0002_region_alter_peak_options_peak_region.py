# Generated by Django 4.2.7 on 2023-12-05 13:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("peaks", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Region",
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
                ("name", models.CharField(max_length=200)),
                ("country_code", models.CharField(max_length=2)),
            ],
        ),
        migrations.AlterModelOptions(
            name="peak",
            options={"ordering": ["unicode_name"]},
        ),
        migrations.AddField(
            model_name="peak",
            name="region",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="peaks.region",
            ),
        ),
    ]
