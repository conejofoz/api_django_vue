# Generated by Django 4.0.1 on 2022-07-20 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0060_cliente_nacional'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='endereco_nf',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]