# Generated by Django 3.2.11 on 2022-04-13 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_venda_paga'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstoqueEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.FloatField(default=0)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresa_estoque', to='api.empresa')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='empresa_estoque', to='api.produto')),
            ],
        ),
        migrations.AddField(
            model_name='produto',
            name='empresa',
            field=models.ManyToManyField(related_name='empresas', through='api.EstoqueEmpresa', to='api.Empresa'),
        ),
    ]
