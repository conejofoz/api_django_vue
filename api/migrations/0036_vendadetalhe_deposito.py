# Generated by Django 4.0.1 on 2022-05-19 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_estoqueempresa_deposito1_estoqueempresa_deposito2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendadetalhe',
            name='deposito',
            field=models.IntegerField(default=0),
        ),
    ]
