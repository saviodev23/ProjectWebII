# Generated by Django 4.2.8 on 2024-01-10 12:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='criado_em',
            field=models.DateTimeField(default=datetime.date(2024, 1, 10)),
        ),
    ]