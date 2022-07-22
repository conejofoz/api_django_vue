# Generated by Django 4.0.1 on 2022-07-18 14:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0057_produtoantigo_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='venda',
            name='extenso',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='venda',
            name='numero_nf',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.CreateModel(
            name='NotaFiscal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('sucursal', models.CharField(max_length=3)),
                ('pdv', models.CharField(max_length=3)),
                ('numero', models.IntegerField(default=0)),
                ('numero_final', models.IntegerField(default=0)),
                ('descricao', models.CharField(max_length=100)),
                ('uc', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('um', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]