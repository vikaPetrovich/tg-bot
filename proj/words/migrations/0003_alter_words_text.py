# Generated by Django 4.1.1 on 2022-09-17 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_alter_words_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='words',
            name='text',
            field=models.TextField(max_length=400, verbose_name='Quote'),
        ),
    ]