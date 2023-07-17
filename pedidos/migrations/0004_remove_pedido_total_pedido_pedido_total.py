# Generated by Django 4.2.3 on 2023-07-11 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_pedido_produtos_alter_pedido_total_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='total_pedido',
        ),
        migrations.AddField(
            model_name='pedido',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
