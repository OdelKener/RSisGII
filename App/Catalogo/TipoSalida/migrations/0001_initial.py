# Generated by Django 4.2 on 2024-11-05 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoSalida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(choices=[('compras', 'Compras'), ('devolucion', 'Devolución')], max_length=100, verbose_name='Nombres')),
            ],
            options={
                'verbose_name': 'TiposSalidas',
            },
        ),
    ]