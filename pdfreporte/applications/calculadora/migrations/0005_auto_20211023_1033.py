# Generated by Django 3.0.6 on 2021-10-23 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora', '0004_auto_20211023_0928'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='laplace',
            options={},
        ),
        migrations.RemoveField(
            model_name='laplace',
            name='denominador',
        ),
        migrations.RemoveField(
            model_name='laplace',
            name='numerador',
        ),
        migrations.RemoveField(
            model_name='laplace',
            name='tota',
        ),
        migrations.RemoveField(
            model_name='laplace',
            name='var3',
        ),
        migrations.RemoveField(
            model_name='laplace',
            name='var_2',
        ),
        migrations.RemoveField(
            model_name='laplace',
            name='var_s_1',
        ),
        migrations.RemoveField(
            model_name='laplace',
            name='var_s_2',
        ),
        migrations.AlterField(
            model_name='laplace',
            name='var_1',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
