# Generated by Django 4.2.16 on 2025-01-18 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0033_interactiveactivity_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interactiveactivity',
            name='index',
        ),
        migrations.AlterField(
            model_name='interactiveactivity',
            name='html_file_name',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
    ]
