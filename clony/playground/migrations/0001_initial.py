# Generated by Django 5.1.6 on 2025-02-13 13:15

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ProblemSelection',
            fields=[
                ('title', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('create_date', models.DateField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Problem Selection',
                'verbose_name_plural': 'Problem Selections',
            },
        ),
        migrations.CreateModel(
            name='InteractiveActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('grades_and_difficulty', models.CharField(blank=True, max_length=200, null=True)),
                ('problem_statement', models.TextField(blank=True, null=True)),
                ('topic_tags', models.CharField(blank=True, max_length=300, null=True)),
                ('answer', models.CharField(blank=True, max_length=1000, null=True)),
                ('html_file_name', models.CharField(blank=True, max_length=200, null=True, unique=True)),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('grades_and_difficulty', models.CharField(blank=True, max_length=200, null=True)),
                ('problem_statement', models.TextField(blank=True, null=True)),
                ('topic_tags', models.CharField(blank=True, max_length=300, null=True)),
                ('type', models.CharField(blank=True, choices=[('input-integer', 'input-integer'), ('input-text', 'input-text'), ('multiple choice-text', 'multiple choice-text'), ('multiple choice-image', 'multiple choice-image'), ('multiple selection-text', 'multiple selection-text'), ('multiple selection-image', 'multiple selection-image'), ('interactive', 'interactive')], max_length=200, null=True)),
                ('source_type', models.CharField(blank=True, choices=[('translation', 'translation'), ('designed', 'designed')], max_length=200, null=True)),
                ('answer', models.CharField(blank=True, max_length=200, null=True)),
                ('text_choices', models.TextField(blank=True, max_length=1000, null=True)),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='StationBasedEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('audience', models.CharField(blank=True, max_length=1000, null=True)),
                ('start_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('role', models.CharField(blank=True, choices=[(1, 'coordinator'), (2, 'event staff'), (3, 'admin')], max_length=20, null=True)),
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
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('k12_section', models.CharField(blank=True, choices=[(1, '(1-6)'), (2, '(7-9)'), (3, '(10-12)'), (4, '(1-9'), (5, '(7-12'), (6, '1-12')], max_length=200, null=True)),
                ('province', models.CharField(blank=True, max_length=200, null=True)),
                ('gender', models.CharField(blank=True, choices=[(1, 'female'), (2, 'male')], max_length=200, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('population', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'verbose_name': 'Institution',
                'verbose_name_plural': 'Institutions',
            },
            bases=('playground.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('problemselection_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='playground.problemselection')),
                ('is_quiz', models.BooleanField(default=False)),
            ],
            bases=('playground.problemselection',),
        ),
        migrations.AddField(
            model_name='problemselection',
            name='problems',
            field=models.ManyToManyField(to='playground.problem'),
        ),
        migrations.CreateModel(
            name='ProblemAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_answer', models.CharField(blank=True, max_length=400, null=True)),
                ('is_correct', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('score_type', models.CharField(blank=True, max_length=200, null=True)),
                ('score', models.IntegerField(default=0)),
                ('note', models.TextField(blank=True, null=True)),
                ('problem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='playground.problem')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='playground.station')),
            ],
        ),
        migrations.CreateModel(
            name='InteractiveAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_answer', models.CharField(blank=True, max_length=400, null=True)),
                ('is_correct', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('score_type', models.CharField(blank=True, max_length=200, null=True)),
                ('score', models.IntegerField(default=0)),
                ('note', models.TextField(blank=True, null=True)),
                ('activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='playground.interactiveactivity')),
                ('student', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='playground.station')),
            ],
        ),
        migrations.CreateModel(
            name='EventAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_problem', models.BooleanField(blank=True, null=True)),
                ('student_answer', models.CharField(blank=True, max_length=1000, null=True)),
                ('is_correct', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('participant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('interactive_activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='playground.interactiveactivity')),
                ('problem', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='playground.problem')),
                ('station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='playground.station')),
            ],
        ),
        migrations.AddField(
            model_name='station',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='playground.stationbasedevent'),
        ),
        migrations.CreateModel(
            name='StationInteractiveActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.interactiveactivity')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.station')),
            ],
            options={
                'ordering': ['order'],
                'unique_together': {('station', 'activity')},
            },
        ),
        migrations.AddField(
            model_name='station',
            name='activities',
            field=models.ManyToManyField(blank=True, null=True, through='playground.StationInteractiveActivity', to='playground.interactiveactivity'),
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
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('grade', models.IntegerField(blank=True, default=0, null=True)),
                ('coins', models.IntegerField(blank=True, default=0, null=True)),
                ('school_name', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('id_number', models.CharField(blank=True, max_length=20, null=True)),
                ('province', models.CharField(blank=True, max_length=100, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Student',
                'verbose_name_plural': 'Students',
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='playground.admin')),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('institution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='playground.institution')),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('problemselection_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='playground.problemselection')),
                ('is_challenge', models.BooleanField(default=False)),
                ('organizer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='playground.institution')),
            ],
            bases=('playground.problemselection',),
        ),
    ]
