# Generated by Django 5.1.3 on 2024-11-21 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flipkart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specifications',
            field=models.TextField(default=2, max_length=1000),
        ),
    ]
