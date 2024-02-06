
# Generated by Django 4.2.8 on 2024-01-09 12:48


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
            name='Parametro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('valor', models.IntegerField(default=30)),
                ('criado_em', models.DateField(default=datetime.date(2024, 1, 9))),
                ('criado_por', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Disponibilidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia', models.CharField(choices=[('Segunda', 'Segunda-Feira'), ('Terça', 'Terça-Feira'), ('Quarta', 'Quarta-Feira'), ('Quinta', 'Quinta-Feira'), ('Sexta', 'Sexta-Feira')], max_length=20)),
                ('horario_inicio', models.TimeField(default=datetime.time(0, 0))),
                ('horario_fim', models.TimeField(default=datetime.time(0, 0))),
                ('profissional', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]