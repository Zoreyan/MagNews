# Generated by Django 4.2 on 2023-05-06 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='news_images/', verbose_name='Картинка')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
