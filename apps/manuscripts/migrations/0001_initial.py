# Generated by Django 5.1.1 on 2024-10-04 01:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True)),
                ('shelfmark', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ItemFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ItemImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='historical_items')),
                ('locus', models.CharField(max_length=20, null=True)),
                ('folio_side', models.CharField(max_length=20, null=True)),
                ('folio_number', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('label', models.CharField(max_length=30)),
                ('place', models.CharField(max_length=50)),
                ('url', models.URLField(null=True)),
                ('type', models.CharField(choices=[('Library', 'Library'), ('Institution', 'Institution'), ('Person', 'Person'), ('Online Resource', 'Online Resource')], max_length=30, null=True)),
            ],
            options={
                'verbose_name_plural': 'Repositories',
            },
        ),
        migrations.CreateModel(
            name='HistoricalItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Agreement', 'Agreement'), ('Charter', 'Charter'), ('Letter', 'Letter')], max_length=20)),
                ('language', models.CharField(max_length=100)),
                ('vernacular', models.BooleanField(null=True)),
                ('neumed', models.BooleanField(null=True)),
                ('hair_type', models.CharField(choices=[('FHFH', 'FHFH'), ('FHHF', 'FHHF'), ('HFFH', 'HFFH'), ('HFHF', 'HFHF'), ('Mixed', 'Mixed')], max_length=20, null=True)),
                ('date', models.CharField(max_length=100)),
                ('date_sort', models.CharField(max_length=100)),
                ('issuer', models.CharField(max_length=100)),
                ('named_beneficiary', models.CharField(max_length=100)),
                ('format', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='manuscripts.itemformat')),
            ],
        ),
        migrations.CreateModel(
            name='ImageText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('type', models.CharField(choices=[('Transcription', 'Transcription'), ('Translation', 'Translation')], max_length=13)),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Review', 'Review'), ('Live', 'Live')], max_length=6)),
                ('item_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuscripts.itemimage')),
            ],
        ),
        migrations.CreateModel(
            name='ItemPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuscripts.currentitem')),
                ('historical_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuscripts.historicalitem')),
            ],
        ),
        migrations.AddField(
            model_name='itemimage',
            name='item_part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuscripts.itempart'),
        ),
        migrations.CreateModel(
            name='HistoricalItemDescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('historical_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='manuscripts.historicalitem')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuscripts.repository')),
            ],
        ),
        migrations.AddField(
            model_name='currentitem',
            name='repository',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuscripts.repository'),
        ),
        migrations.CreateModel(
            name='CatalogueNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=30)),
                ('url', models.URLField(null=True)),
                ('historical_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catalogue_numbers', to='manuscripts.historicalitem')),
                ('catalogue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manuscripts.repository')),
            ],
        ),
    ]
