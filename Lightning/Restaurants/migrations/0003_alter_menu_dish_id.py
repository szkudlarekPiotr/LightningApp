# Generated by Django 4.2.6 on 2023-10-11 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurants', '0002_remove_menu_id_alter_menu_dish_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='dish_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='Restaurants.dish'),
        ),
    ]
