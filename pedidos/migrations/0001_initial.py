# Generated by Django 4.2.3 on 2023-07-10 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('produtos', '0002_produto_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_cliente', models.CharField(max_length=100)),
                ('status_pedido', models.CharField(choices=[('preparando', 'Preparando'), ('pronto', 'Pronto'), ('entregue', 'Entregue'), ('cancelado', 'Cancelado')], default='preparando', max_length=20)),
                ('total_pedido', models.DecimalField(decimal_places=2, max_digits=8)),
                ('observacao', models.TextField(blank=True)),
                ('pagamento', models.CharField(choices=[('dinheiro', 'Dinheiro'), ('pix', 'PIX'), ('credito', 'Crédito'), ('debito', 'Débito'), ('vale', 'Vale')], max_length=20)),
                ('produtos', models.ManyToManyField(through='pedidos.ItemPedido', to='produtos.produto')),
            ],
        ),
        migrations.AddField(
            model_name='itempedido',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedido'),
        ),
        migrations.AddField(
            model_name='itempedido',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.produto'),
        ),
    ]
