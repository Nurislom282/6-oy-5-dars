# Generated by Django 5.1.3 on 2024-12-03 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cars',
            name='model',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='new.models', verbose_name='modelni kiriting'),
            preserve_default=False,
        ),
    ]