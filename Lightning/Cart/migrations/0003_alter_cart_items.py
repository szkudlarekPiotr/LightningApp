# Generated by Django 4.2.6 on 2023-10-17 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0002_alter_cart_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.CharField(),
        ),
    ]