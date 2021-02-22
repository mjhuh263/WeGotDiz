# Generated by Django 3.1.6 on 2021-02-21 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MakerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('reputation_level', models.DecimalField(decimal_places=1, max_digits=2)),
                ('communication_level', models.DecimalField(decimal_places=1, max_digits=2)),
                ('popularity_level', models.DecimalField(decimal_places=1, max_digits=2)),
            ],
            options={
                'db_table': 'makers_info',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('image', models.URLField(max_length=2000)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('maker_info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.makerinfo')),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
