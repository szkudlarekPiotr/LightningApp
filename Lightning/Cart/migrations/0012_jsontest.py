# Generated by Django 4.2.6 on 2023-11-03 13:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Cart", "0011_alter_cart_owner"),
    ]

    operations = [
        migrations.CreateModel(
            name="JsonTest",
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
                ("test", models.JSONField(null=True)),
            ],
        ),
    ]
