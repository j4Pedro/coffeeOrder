# Generated by Django 3.0 on 2020-04-07 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0002_auto_20200403_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=100, verbose_name='總金額')),
                ('remark', models.TextField(blank=True, null=True, verbose_name='說明')),
                ('price', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='價格')),
                ('products', models.ManyToManyField(blank=True, null=True, to='products.Product')),
            ],
        ),
    ]
