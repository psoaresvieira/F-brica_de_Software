# Generated by Django 4.1.7 on 2023-04-01 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChampionsLeague',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temporada', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('estadio', models.CharField(max_length=40)),
                ('temporada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Time', to='liga.championsleague')),
            ],
        ),
        migrations.CreateModel(
            name='Jogador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('posicao', models.CharField(max_length=100)),
                ('time', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Jogador', to='liga.time')),
            ],
        ),
    ]