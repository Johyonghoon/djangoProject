# Generated by Django 4.1.3 on 2022-11-30 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=255)),
                ('detail_address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_users.shopuser')),
            ],
            options={
                'db_table': 'shop_deliveries',
            },
        ),
    ]
