# Generated by Django 3.2.11 on 2022-03-19 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_alter_moeda_empresa'),
    ]

    operations = [
        migrations.CreateModel(
            name='LancamentoCaixa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('controle', models.CharField(blank=True, max_length=100, null=True)),
                ('data', models.DateField()),
                ('descricao', models.CharField(max_length=200)),
                ('siglaMoeda', models.CharField(max_length=2)),
                ('tipo', models.CharField(max_length=1)),
                ('valor1', models.FloatField(default=0)),
                ('cotacao', models.FloatField(default=0)),
                ('valor2', models.FloatField(default=0)),
                ('empresa', models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, to='api.empresa')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
