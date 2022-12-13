# Generated by Django 4.1 on 2022-12-13 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('code', models.CharField(max_length=255, verbose_name='Артикул')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('status', models.CharField(choices=[('in_stock', 'В наличии'), ('on_order', 'Под заказ'), ('waiting', 'Ожидается поступление'), ('no_in_stock', 'Нет в наличии'), ('not_produced', 'Не производится')], max_length=255, verbose_name='Статус')),
                ('image', models.ImageField(upload_to='images', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['title'],
            },
        ),
    ]