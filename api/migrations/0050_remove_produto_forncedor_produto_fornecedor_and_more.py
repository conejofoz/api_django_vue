# Generated by Django 4.0.1 on 2022-07-02 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0049_produto_classificacaodi_produto_codigo_barras_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='forncedor',
        ),
        migrations.AddField(
            model_name='produto',
            name='fornecedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='fornecedores', to='api.fornecedor'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='grupo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='grupos', to='api.grupo'),
        ),
    ]