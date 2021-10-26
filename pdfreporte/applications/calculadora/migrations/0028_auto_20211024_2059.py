# Generated by Django 3.0.4 on 2021-10-25 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora', '0027_auto_20211024_2058'),
    ]

    operations = [
        migrations.CreateModel(
            name='laplace_9',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('var_1', models.IntegerField()),
                ('var_2', models.IntegerField()),
                ('resultado', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'verbose_name': 't^ e^at = nb/(s-a)^n+1 ',
                'verbose_name_plural': 't^ e^at = nb/(s-a)^n+1 ',
            },
        ),
        migrations.AlterModelOptions(
            name='laplace_7',
            options={'verbose_name': 'cos at = s/s^4 a^2', 'verbose_name_plural': 'cos at = s/s^4 a^2'},
        ),
        migrations.RemoveField(
            model_name='laplace_7',
            name='var_2',
        ),
    ]
