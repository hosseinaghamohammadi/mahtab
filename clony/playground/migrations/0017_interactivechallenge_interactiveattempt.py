# Generated by Django 4.2.16 on 2025-01-16 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0016_rename_timestamp_attempt_created_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='InteractiveChallenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('grades_and_difficulty', models.CharField(blank=True, max_length=200, null=True)),
                ('problem_statement', models.TextField(blank=True, null=True)),
                ('topic_tags', models.CharField(blank=True, max_length=300, null=True)),
                ('answer', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='InteractiveAttempt',
            fields=[
                ('attempt_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='playground.attempt')),
                ('challenge', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.interactivechallenge')),
            ],
            bases=('playground.attempt',),
        ),
    ]
