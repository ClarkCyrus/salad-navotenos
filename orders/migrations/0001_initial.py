# Generated by Django 5.0.4 on 2024-05-11 06:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crochet_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('total_price', models.FloatField()),
                ('shipping_fee', models.FloatField()),
                ('shipping_address', models.TextField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Salad_Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Processing', 'Processing'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Cancelled', 'Cancelled')], default='Pending', max_length=20)),
                ('created', models.DateField(auto_now_add=True)),
                ('shipping_fee', models.FloatField()),
                ('total_price', models.FloatField()),
                ('shipping_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Crochet_Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateField(auto_now_add=True)),
                ('total_price', models.FloatField()),
                ('shipping_fee', models.FloatField()),
                ('shipping_address', models.TextField()),
                ('crochet_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_orders', to='orders.crochet_order')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
