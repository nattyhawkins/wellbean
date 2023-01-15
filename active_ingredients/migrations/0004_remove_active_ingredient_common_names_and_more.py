# Generated by Django 4.1.4 on 2023-01-15 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('active_ingredients', '0003_remove_active_ingredient_mediums'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='active_ingredient',
            name='common_names',
        ),
        migrations.AlterField(
            model_name='active_ingredient',
            name='description',
            field=models.TextField(max_length=50000),
        ),
    ]
