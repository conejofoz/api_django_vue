# Generated by Django 4.0.1 on 2022-07-04 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0051_rename_peso_neto_bruto_produto_peso_bruto_caixa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='peso_bruto_caixa',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='peso_neto_caixa',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_atacado',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_atacado_dp',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_custo',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_custo_di',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_custo_dp',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_ficticio_dp',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_medio',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_origem_dp',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='produto',
            name='quantidade_por_caixa',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]