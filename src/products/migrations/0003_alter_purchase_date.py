# Generated by Django 4.1.3 on 2022-12-03 13:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_alter_product_date_purchase"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchase",
            name="date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
