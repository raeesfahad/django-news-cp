# Generated by Django 4.2.1 on 2023-06-06 13:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0003_remove_news_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]