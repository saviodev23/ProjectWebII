# Generated by Django 4.2.8 on 2024-02-03 20:17

from datetime import date
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0011_alter_agendamento_criado_em'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamento',
            name='quantidade_concluido',
        ),
        migrations.AlterField(
            model_name='agendamento',
            name='criado_em',
            field=models.DateTimeField(default=date(2024, 2, 3)),
        ),
    ]