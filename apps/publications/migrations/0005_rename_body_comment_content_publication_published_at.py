# Generated by Django 5.1.1 on 2024-09-24 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0004_event_slug_alter_publication_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='content',
        ),
        migrations.AddField(
            model_name='publication',
            name='published_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]