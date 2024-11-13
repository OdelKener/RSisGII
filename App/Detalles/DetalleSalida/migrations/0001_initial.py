# Generated by Django 4.2 on 2024-11-05 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('LibrosCos', '0001_initial'),
        ('Libros', '0001_initial'),
        ('LibrosHon', '0001_initial'),
        ('LibrosPan', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetalleSalida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('costosalida', models.BigIntegerField(blank=True, null=True, verbose_name='CostoSalida')),
                ('cantidad', models.BigIntegerField(blank=True, null=True, verbose_name='Cantidad')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Libros.libro', verbose_name='Libro')),
                ('librocos', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='LibrosCos.libroscos', verbose_name='LibroCos')),
                ('librohon', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='LibrosHon.libroshon', verbose_name='LibroHon')),
                ('libropan', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='LibrosPan.librospan', verbose_name='LibroPan')),
            ],
        ),
    ]