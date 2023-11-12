# Generated by Django 4.2.6 on 2023-11-06 18:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Cart", "0013_rename_test_jsontest_products"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="item",
        ),
        migrations.RemoveField(
            model_name="cart",
            name="quantity",
        ),
        migrations.AddField(
            model_name="cart",
            name="products",
            field=models.JSONField(default=1),
            preserve_default=False,
        ),
    ]