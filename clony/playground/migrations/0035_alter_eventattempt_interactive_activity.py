# Generated by Django 4.2.16 on 2025-01-21 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0034_remove_interactiveactivity_index_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventattempt',
            name='interactive_activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='playground.interactiveactivity'),
        ),
    ]
