# Generated by Django 4.2.6 on 2023-10-17 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cart', '0003_alter_cart_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='items',
            new_name='item',
        ),
    ]