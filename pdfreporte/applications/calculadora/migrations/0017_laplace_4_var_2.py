# Generated by Django 3.0.4 on 2021-10-24 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora', '0016_auto_20211024_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='laplace_4',
            name='var_2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
