# Generated by Django 3.2.2 on 2022-02-24 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='market',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='market',
            name='updated_at',
        ),
    ]
