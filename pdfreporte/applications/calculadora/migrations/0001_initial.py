# Generated by Django 3.0.6 on 2021-10-22 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='laplace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('var_1', models.IntegerField(blank=True, null=True)),
                ('var_2', models.IntegerField(blank=True, null=True)),
                ('var3', models.IntegerField(blank=True, null=True)),
                ('var_s_1', models.IntegerField()),
                ('var_s_2', models.IntegerField()),
                ('numerador', models.CharField(blank=True, max_length=15, null=True)),
                ('denominador', models.CharField(blank=True, max_length=15, null=True)),
                ('tota', models.CharField(blank=True, max_length=15, null=True, verbose_name='Resultado')),
            ],
            options={
                'verbose_name': 't^n = n!/sn^1',
                'verbose_name_plural': 't^n = n!/sn^1',
            },
        ),
        migrations.CreateModel(
            name='laplace_2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variable_1', models.CharField(max_length=30)),
            ],
        ),
    ]
