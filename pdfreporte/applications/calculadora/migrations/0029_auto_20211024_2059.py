# Generated by Django 3.0.4 on 2021-10-25 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora', '0028_auto_20211024_2059'),
    ]

    operations = [
        migrations.DeleteModel(
            name='laplace_9',
        ),
        migrations.AlterModelOptions(
            name='laplace_8',
            options={'verbose_name': 't^ e^at = nb/(s-a)^n+1 ', 'verbose_name_plural': 't^ e^at = nb/(s-a)^n+1 '},
        ),
        migrations.AddField(
            model_name='laplace_8',
            name='var_2',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
