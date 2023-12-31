# Generated by Django 4.2.2 on 2023-06-12 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating_avg',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='rating_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movie',
            name='ratings_total',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
