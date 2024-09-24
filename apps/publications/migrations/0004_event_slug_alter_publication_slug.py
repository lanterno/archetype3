# Generated by Django 5.1.1 on 2024-09-24 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0003_remove_publication_tags_alter_publication_keywords_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='slug',
            field=models.SlugField(default='111', max_length=150, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publication',
            name='slug',
            field=models.SlugField(max_length=150, unique=True),
        ),
    ]