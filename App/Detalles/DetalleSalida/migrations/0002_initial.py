# Generated by Django 4.2 on 2024-11-05 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Salida', '0001_initial'),
        ('DetalleSalida', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='detallesalida',
            name='salida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Salida.salida', verbose_name='Salida'),
        ),
    ]
