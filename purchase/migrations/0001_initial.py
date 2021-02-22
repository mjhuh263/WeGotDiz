# Generated by Django 3.1.6 on 2021-02-21 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user')),
            ],
            options={
                'db_table': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=45)),
                ('contact_number', models.CharField(max_length=20)),
                ('delivery_note', models.CharField(max_length=50, null=True)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('delivery_fee', models.DecimalField(decimal_places=2, default=2500, max_digits=10)),
                ('donation', models.DecimalField(decimal_places=1, max_digits=2, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('order_status', models.CharField(default='결제완료', max_length=45)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='purchase.address')),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='RewardOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='purchase.order')),
                ('reward', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.reward')),
            ],
            options={
                'db_table': 'rewards_orders',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='reward',
            field=models.ManyToManyField(through='purchase.RewardOrder', to='product.Reward'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user'),
        ),
    ]
