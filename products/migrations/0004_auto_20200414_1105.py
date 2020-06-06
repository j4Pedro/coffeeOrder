# Generated by Django 3.0 on 2020-04-14 03:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_productvariation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productvariation',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.ProductImage'),
        ),
    ]