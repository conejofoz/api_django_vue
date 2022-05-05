# Generated by Django 3.2.11 on 2022-03-12 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_auto_20220310_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='Moeda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('descricao', models.CharField(max_length=50)),
                ('sigla', models.CharField(max_length=3)),
                ('cotacao', models.FloatField(default=0)),
                ('acrescimo', models.FloatField(default=0)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.empresa')),
            ],
            options={
                'verbose_name_plural': 'moedas',
            },
        ),
    ]