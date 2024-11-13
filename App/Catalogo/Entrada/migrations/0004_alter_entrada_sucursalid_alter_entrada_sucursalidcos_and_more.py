# Generated by Django 4.2 on 2024-11-12 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Nicaragua', '0001_initial'),
        ('Hondura', '0002_alter_sucursalhon_options'),
        ('CostaRica', '0002_alter_sucursalcos_options'),
        ('Panama', '0001_initial'),
        ('Entrada', '0003_alter_entrada_sucursalid_alter_entrada_sucursalidcos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrada',
            name='sucursalid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Nicaragua.sucursal', verbose_name='Sucursal'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='sucursalidcos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='CostaRica.sucursalcos', verbose_name='SucursalCos'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='sucursalidhon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Hondura.sucursalhon', verbose_name='SucursalHon'),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='sucursalidpan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='Panama.sucursalpan', verbose_name='SucursalPan'),
        ),
    ]
