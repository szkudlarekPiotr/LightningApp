# Generated by Django 4.2.6 on 2023-11-03 17:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Cart", "0012_jsontest"),
    ]

    operations = [
        migrations.RenameField(
            model_name="jsontest",
            old_name="test",
            new_name="products",
        ),
    ]
