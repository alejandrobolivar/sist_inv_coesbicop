# Generated by Django 3.1.5 on 2021-01-21 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entrega', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrega',
            name='cod_med',
            field=models.CharField(default='', max_length=10),
        ),
    ]
