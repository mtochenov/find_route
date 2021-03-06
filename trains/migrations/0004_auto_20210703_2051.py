# Generated by Django 3.2.3 on 2021-07-03 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0002_auto_20210622_1358'),
        ('trains', '0003_alter_train_departure_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='train',
            name='departure_city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='departure_city_set', to='cities.city', verbose_name='Город отправления'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='train',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Номер поезда'),
        ),
        migrations.DeleteModel(
            name='TrainTest',
        ),
    ]
