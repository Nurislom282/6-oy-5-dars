# Generated by Django 5.1.3 on 2024-12-04 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new', '0002_cars_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='models',
            name='model_logo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/', verbose_name='model rasmi'),
        ),
    ]
