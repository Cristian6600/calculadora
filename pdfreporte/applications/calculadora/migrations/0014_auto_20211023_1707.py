# Generated by Django 3.0.6 on 2021-10-23 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora', '0013_auto_20211023_1653'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='laplace_3',
            options={'verbose_name': '1/S-a', 'verbose_name_plural': '1/S-a'},
        ),
        migrations.AlterField(
            model_name='laplace_3',
            name='resultado',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
