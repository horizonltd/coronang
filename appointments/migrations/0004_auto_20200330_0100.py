# Generated by Django 3.0.3 on 2020-03-30 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0003_auto_20200330_0045'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='test_id',
        ),
        migrations.AddField(
            model_name='appointment',
            name='code',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
    ]
