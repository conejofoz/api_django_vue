# Generated by Django 3.2.11 on 2022-02-05 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_venda_vendadetalhe'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
