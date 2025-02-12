# Generated by Django 4.2.16 on 2024-10-23 23:39

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('playground', '0002_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('grade', models.IntegerField(blank=True, default=0, null=True)),
                ('coins', models.IntegerField(blank=True, default=0, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('school_name', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('id_number', models.CharField(blank=True, max_length=20, null=True)),
                ('province', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('playground.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
