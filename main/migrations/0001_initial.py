# Generated by Django 2.2 on 2021-10-30 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length='32')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length='32')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Commission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length='32')),
                ('percentage', models.FloatField()),
            ],
            options={
                'verbose_name': 'Comision',
                'verbose_name_plural': 'Comisiones',
            },
        ),
        migrations.CreateModel(
            name='Creditor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length='32')),
            ],
            options={
                'verbose_name': 'Acreedor',
                'verbose_name_plural': 'Acreedores',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length='32')),
                ('symbol', models.TextField(max_length='4')),
            ],
            options={
                'verbose_name': 'Moneda',
                'verbose_name_plural': 'Monedas',
            },
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.TextField(choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')])),
                ('year', models.PositiveSmallIntegerField()),
                ('type_of_pay', models.TextField(choices=[('1', 'Interno'), ('2', 'Externo')])),
                ('subtotal_available', models.FloatField()),
                ('total_available', models.FloatField()),
                ('total_invested', models.FloatField()),
                ('total_comsissions', models.FloatField()),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Brand')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Client')),
                ('creditor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Creditor')),
            ],
            options={
                'verbose_name': 'Plan de Medios',
                'verbose_name_plural': 'Planes de Medios',
            },
        ),
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campaign', models.TextField(max_length='32')),
                ('medio', models.TextField(max_length='32')),
                ('format', models.TextField(max_length='32')),
                ('value', models.FloatField()),
                ('available_value', models.FloatField()),
                ('month', models.TextField(choices=[('Enero', 'Enero'), ('Febrero', 'Febrero'), ('Marzo', 'Marzo'), ('Abril', 'Abril'), ('Mayo', 'Mayo'), ('Junio', 'Junio'), ('Julio', 'Julio'), ('Agosto', 'Agosto'), ('Septiembre', 'Septiembre'), ('Octubre', 'Octubre'), ('Noviembre', 'Noviembre'), ('Diciembre', 'Diciembre')])),
                ('year', models.PositiveSmallIntegerField()),
                ('brand_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Brand')),
                ('client_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Client')),
                ('commission', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Commission')),
            ],
            options={
                'verbose_name': 'Inversion',
                'verbose_name_plural': 'Inversiones',
            },
        ),
        migrations.AddField(
            model_name='brand',
            name='client_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Client'),
        ),
    ]
