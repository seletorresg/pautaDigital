# Generated by Django 2.2 on 2021-10-24 06:36

from django.db import migrations, models
import main.models.invoice


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211024_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='file',
            field=models.FileField(upload_to=main.models.invoice.upload_invoice),
        ),
    ]