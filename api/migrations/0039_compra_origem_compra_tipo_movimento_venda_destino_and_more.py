# Generated by Django 4.0.1 on 2022-06-08 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0038_remove_compra_cornecedor_compra_fornecedor'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='origem',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='compra',
            name='tipo_movimento',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='venda',
            name='destino',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='venda',
            name='tipo_movimento',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
