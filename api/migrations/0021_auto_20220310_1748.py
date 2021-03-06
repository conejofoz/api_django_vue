# Generated by Django 3.2.11 on 2022-03-10 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0020_alter_venda_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='total',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='produto',
            name='subcategoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.subcategoria'),
        ),
        migrations.AlterField(
            model_name='subcategoria',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subcategorias', to='api.categoria'),
        ),
    ]
