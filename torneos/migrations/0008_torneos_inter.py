# Generated by Django 2.2.28 on 2023-04-14 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torneos', '0007_auto_20230414_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='torneos',
            name='inter',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]