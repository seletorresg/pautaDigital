# Generated by Django 2.2 on 2021-10-24 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20211024_0040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='investment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Investment'),
        ),
    ]