# Generated by Django 3.0.6 on 2021-10-22 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculadora', '0002_auto_20211022_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='guia',
            name='pru',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
