# Generated by Django 4.0.1 on 2022-06-28 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0046_alter_contacontabil_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='lancamentocaixa',
            name='comprovante',
            field=models.FileField(blank=True, null=True, upload_to='uploads/lancamentos/'),
        ),
    ]
