# Generated by Django 4.2.17 on 2025-01-19 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_user_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.IntegerField(verbose_name='Возраст клиента'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Имя клиента'),
        ),
    ]
