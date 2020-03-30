# Generated by Django 3.0.3 on 2020-03-30 00:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_id', models.CharField(blank=True, max_length=255)),
                ('appointment_date', models.TimeField(blank=True)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_Name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('sex', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('lga', models.CharField(max_length=50)),
                ('ward', models.CharField(max_length=50)),
                ('polling_unit', models.CharField(max_length=50)),
                ('prepared_state_of_testing', models.CharField(max_length=50)),
                ('phone_numbr', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-appointment_date'],
            },
        ),
    ]
