# Generated by Django 5.1.3 on 2024-11-22 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flipkart', '0002_product_specifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='ratings',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=2),
        ),
    ]
