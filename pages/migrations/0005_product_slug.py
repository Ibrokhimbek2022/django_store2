# Generated by Django 4.2 on 2023-04-30 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_subcategory_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, default='', null=True),
        ),
    ]