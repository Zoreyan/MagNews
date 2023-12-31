# Generated by Django 4.2 on 2023-04-28 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Телефонный номер'),
        ),
        migrations.AlterField(
            model_name='user',
            name='telegram',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Telegram'),
        ),
        migrations.AlterField(
            model_name='user',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=12, null=True, verbose_name='Whatsapp'),
        ),
    ]
