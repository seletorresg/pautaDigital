# Generated by Django 2.2 on 2021-10-24 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20211024_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.TextField(max_length='16'),
        ),
    ]
