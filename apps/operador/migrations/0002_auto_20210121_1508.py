# Generated by Django 3.1.5 on 2021-01-21 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operador', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operador',
            name='id_operador',
        ),
        migrations.AddField(
            model_name='operador',
            name='usuario_operador',
            field=models.CharField(default='', max_length=200),
        ),
    ]