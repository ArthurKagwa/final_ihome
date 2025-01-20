# Generated by Django 5.1.5 on 2025-01-20 13:05

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to.', related_name='farm_user_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='farm_user_set', to='auth.permission', verbose_name='user permissions')),
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
            name='Breed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed_origin', models.CharField(max_length=10)),
                ('breed_name', models.CharField(max_length=50)),
                ('breed_description', models.CharField(max_length=500)),
                ('farm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Farm.farm')),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('dob', models.DateField()),
                ('sex', models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=1)),
                ('births', models.IntegerField(null=True)),
                ('father', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animal_father', to='Farm.animal')),
                ('mother', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='animal_mother', to='Farm.animal')),
                ('breed', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Farm.breed')),
                ('farm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Farm.farm')),
            ],
        ),
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment_date', models.DateField()),
                ('treatment_name', models.CharField(max_length=50)),
                ('treatment_cost', models.FloatField(null=True)),
                ('treatment_description', models.CharField(max_length=100)),
                ('animal_no', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Farm.animal')),
                ('farm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Farm.farm')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('staff_name', models.CharField(max_length=50)),
                ('staff_address', models.CharField(max_length=100)),
                ('staff_phone', models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^\\d{10}$', message='Phone number must be 10 digits.')])),
                ('staff_email', models.EmailField(max_length=254)),
                ('staff_position', models.CharField(max_length=50)),
                ('staff_nin', models.CharField(max_length=30, unique=True)),
                ('farm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Farm.farm')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('desc', models.CharField(max_length=100)),
                ('farm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Farm.farm')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50)),
                ('task_description', models.CharField(max_length=300)),
                ('task_day', models.DateField()),
                ('task_time', models.TimeField(default='00:00:00')),
                ('task_status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('In Progress', 'In Progress'), ('Cancelled', 'Cancelled')], default='Pending', max_length=40)),
                ('task_notes', models.CharField(default='not bad', max_length=100)),
                ('farm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Farm.farm')),
                ('task_animal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_animal', to='Farm.animal')),
                ('task_staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Farm.staff')),
                ('task_animal_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='task_animal_type', to='Farm.type')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('event_description', models.CharField(max_length=500)),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField()),
                ('event_notes', models.CharField(default='not bad', max_length=100)),
                ('event_status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('In Progress', 'In Progress'), ('Cancelled', 'Cancelled')], default='Pending', max_length=40)),
                ('farm', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Farm.farm')),
                ('event_staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Farm.staff')),
                ('event_animal_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_animal_type', to='Farm.type')),
            ],
        ),
        migrations.AddField(
            model_name='breed',
            name='animal_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Farm.type'),
        ),
        migrations.AddField(
            model_name='animal',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Farm.type'),
        ),
    ]
