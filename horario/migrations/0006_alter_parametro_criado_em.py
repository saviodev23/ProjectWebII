# Generated by Django 4.2.8 on 2024-01-22 14:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horario', '0005_alter_parametro_criado_em'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parametro',
            name='criado_em',
            field=models.DateField(default=datetime.date(2024, 1, 22)),
        ),
    ]
