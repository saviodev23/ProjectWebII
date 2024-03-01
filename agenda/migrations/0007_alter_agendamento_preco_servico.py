# Generated by Django 4.2.8 on 2024-02-27 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0006_agendamento_preco_servico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agendamento',
            name='preco_servico',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço do Serviço'),
        ),
    ]