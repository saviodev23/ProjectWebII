# Generated by Django 4.2.8 on 2024-01-08 03:12

import agenda.models
import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.DateField(help_text='Insira uma data para agenda', validators=[agenda.models.validar_dia])),
                ('horario', models.TimeField()),
                ('status_agendamento', models.CharField(choices=[('AG', 'Agendado'), ('CA', 'Cancelado'), ('CO', 'Concluído')], default='AG', max_length=2)),
                ('criado_em', models.DateTimeField()),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to=settings.AUTH_USER_MODEL)),
                ('criado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='criado_por', to=settings.AUTH_USER_MODEL)),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profissional', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_servico', models.CharField(max_length=50, verbose_name='Nome do Serviço')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço')),
                ('janela_tempo', models.TimeField(default=datetime.time(0, 0), verbose_name='Duração do Serviço')),
                ('imagem', models.ImageField(null=True, upload_to='images/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Fidelidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('CA', 'Cancelado'), ('CO', 'Concluido')], max_length=2)),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.agendamento')),
            ],
        ),
        migrations.AddField(
            model_name='agendamento',
            name='servico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.servico'),
        ),
    ]
