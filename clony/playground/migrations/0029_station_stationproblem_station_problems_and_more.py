# Generated by Django 4.2.16 on 2025-01-17 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0028_remove_eventattempt_station_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('activities', models.ManyToManyField(blank=True, null=True, to='playground.interactiveactivity')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='playground.stationbasedevent')),
            ],
        ),
        migrations.CreateModel(
            name='StationProblem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.problem')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.station')),
            ],
            options={
                'ordering': ['order'],
                'unique_together': {('station', 'problem')},
            },
        ),
        migrations.AddField(
            model_name='station',
            name='problems',
            field=models.ManyToManyField(blank=True, null=True, through='playground.StationProblem', to='playground.problem'),
        ),
        migrations.AddField(
            model_name='eventattempt',
            name='station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='playground.station'),
        ),
        migrations.AddField(
            model_name='interactiveattempt',
            name='station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='playground.station'),
        ),
        migrations.AddField(
            model_name='problemattempt',
            name='station',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='playground.station'),
        ),
    ]
