# Generated by Django 3.1.5 on 2021-01-21 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20210121_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='medicamento',
            field=models.CharField(default='', max_length=10),
        ),
    ]
