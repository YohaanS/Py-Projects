# Generated by Django 4.0.6 on 2024-06-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculateApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation', models.CharField(choices=[('Subtraction', '-'), ('Division', '/'), ('Addition', '+'), ('Multiplication', '*')], max_length=15)),
                ('firstnumber', models.DecimalField(decimal_places=25, max_digits=30)),
                ('secondnumber', models.DecimalField(decimal_places=25, max_digits=30)),
            ],
        ),
        migrations.CreateModel(
            name='VendingMachine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('soda', models.CharField(choices=[('Limca', 'limca'), ('Sprite', 'sprite'), ('Mountain Dew', 'mountain-dew'), ('Fanta', 'fanta'), ('Coca Cola', 'coca-cola'), ('Pepsi', 'pepsi')], max_length=15)),
            ],
        ),
    ]
