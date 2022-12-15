# Generated by Django 4.1.4 on 2022-12-15 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('active_ingredients', '0003_remove_active_ingredient_mediums'),
        ('mediums', '0001_initial'),
        ('recipes', '0002_alter_recipe_description_alter_recipe_inventory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='active_ingredients',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='recipes', to='active_ingredients.active_ingredient'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='mediums',
            field=models.ManyToManyField(blank=True, default=None, null=True, related_name='recipes', to='mediums.medium'),
        ),
    ]
